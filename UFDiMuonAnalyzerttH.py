import sys
import FWCore.ParameterSet.Config as cms
import glob

skim     ="NOSkim"
isMC     = bool(True)
isMSUGRA = bool(False)
isSMS    = bool(False)
useCrab  = bool(False)
doSusyTopProjection = bool(False)
localInFile="/scratch/osg/bregnery/CMSSW_7_4_2/src/ttHmumu/ttHmumu-MINIAOD-*.root"
outputFile="ttHmumu_HighStat_Stage1.root"
#outputFile="SyncOutput/TriggerNamesTest.root"
def getVal(arg):
    i=0
    while i < len(arg) and arg[i] != "=": i+=1
    return arg[i+1:]

## loop over arguments
for i in range(1,len(sys.argv)):
    print "[arg "+str(i)+"] : ", sys.argv[i] 
    if "isMC" in sys.argv[i] :
        isMC=False if getVal(sys.argv[i]) == "False" else True
    elif "isMSUGRA" in sys.argv[i]:
        isMSUGRA=True
    elif "isSMS" in sys.argv[i]:
        isSMS=True
    elif "skim" in sys.argv[i]:
        skim=getVal(sys.argv[i])
    elif "output" in sys.argv[i]:
        outputFile=getVal(sys.argv[i])
    elif "input" in sys.argv[i] :
        localInFile=getVal(sys.argv[i])

inputFiles=glob.glob(localInFile)
inputFiles= ["file:"+x for x in inputFiles]

process = cms.Process("UFDiMuonAnalyzer")

thisIsData = False

if thisIsData:
    print 'Running over data sample'
else:
    print 'Running over MC sample'

process.load("FWCore.MessageService.MessageLogger_cfi")
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
##process.MessageLogger.destinations.append("detailedInfo")
##process.MessageLogger.detailedInfo = cms.untracked.PSet(
##    threshold = cms.untracked.string("INFO"),
##    categories = cms.untracked.vstring("UFHLTTests")
##)

process.load("Configuration.StandardSequences.MagneticField_38T_cff")

## Geometry and Detector Conditions (needed for a few patTuple production steps)

process.load("Configuration.Geometry.GeometryIdeal_cff")

process.load('Configuration.EventContent.EventContent_cff')

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.autoCond import autoCond


# global tag
globalTag = "POSTLS170_V5"
print 'Loading Global Tag: '+globalTag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = globalTag+"::All"


# ------------ PoolSource -------------
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring())
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
# -------- PoolSource END -------------

#===============================================================================

# Clean the Jets from good muons, apply loose jet Id
ccMuPreSel = "pt > 15. && isGlobalMuon "
ccMuPreSel += " && globalTrack().normalizedChi2 < 10 "
ccMuPreSel += " && isPFMuon "
ccMuPreSel += " && innerTrack().hitPattern().trackerLayersWithMeasurement > 5 "
ccMuPreSel += " && innerTrack().hitPattern().numberOfValidPixelHits > 0 "
ccMuPreSel += " && globalTrack().hitPattern().numberOfValidMuonHits > 0 "
ccMuPreSel += " && numberOfMatchedStations > 1 && dB < 0.2 && abs(eta) < 2.4 "
ccMuPreSel += " && ( chargedHadronIso + max(0.,neutralHadronIso + photonIso - 0.5*puChargedHadronIso) ) < 0.12 * pt"

jetSelection = 'neutralEmEnergy/energy < 0.99 '
jetSelection += ' && neutralHadronEnergy/energy < 0.99 '
jetSelection += ' && (chargedMultiplicity + neutralMultiplicity) > 1 '
jetSelection += ' && ((abs(eta)>2.4) || (chargedMultiplicity > 0 '
jetSelection += ' && chargedHadronEnergy/energy > 0.0'
jetSelection += ' && chargedEmEnergy/energy < 0.99))'

process.cleanJets = cms.EDProducer("PATJetCleaner",
          src = cms.InputTag("slimmedJets"),
          preselection = cms.string(jetSelection),
          checkOverlaps = cms.PSet(
             muons = cms.PSet(
               src       = cms.InputTag("slimmedMuons"),
               algorithm = cms.string("byDeltaR"),
               preselection        = cms.string(ccMuPreSel),
               deltaR              = cms.double(0.5),
               checkRecoComponents = cms.bool(False),
               pairCut             = cms.string(""),
               requireNoOverlaps   = cms.bool(True),
             ),
             #electrons = cms.PSet(
             #  src       = cms.InputTag("slimmedElectrons"),
             #  algorithm = cms.string("byDeltaR"),
             #  preselection        = cms.string(ccElePreSel),
             #  deltaR              = cms.double(0.5),
             #  checkRecoComponents = cms.bool(False),
             #  pairCut             = cms.string(""),
             #  requireNoOverlaps   = cms.bool(True),
             #),
         ),
         finalCut = cms.string('')
)

#===============================================================================
# UFDiMuonAnalyzer

if thisIsData:
  process.load("UserArea.UFDiMuonsAnalyzer.UFDiMuonAnalyzer_cff")
else:
  process.load("UserArea.UFDiMuonsAnalyzer.UFDiMuonAnalyzer_MC_cff")

process.dimuons = process.DiMuons.clone()
process.dimuons.pfJetsTag = cms.InputTag("cleanJets")

#===============================================================================

process.p = cms.Path(#
                     process.cleanJets*
                     process.dimuons
                     )


#===============================================================================

# the max events to run over, -1 means all events
process.maxEvents.input = -1

process.source.fileNames.extend(
[
# put the input file names here
# prepend with #"file:" if it is a normal file
# don't prepend anything if it is a file name from DAS
]
)

## input files
#for i in inputFile.split(","):
#   print "Adding: ", i
#   process.source.fileNames.append(i)
#   k = i
process.source.fileNames = cms.untracked.vstring(inputFiles)
   
# The output ntuple name
process.dimuons.getFilename  = cms.untracked.string(outputFile)

### This is for debugging. It spits out a CMSSW ROOT file called dump.root with all of the data types in it
#process.output = cms.OutputModule("PoolOutputModule",
#                                  outputCommands = cms.untracked.vstring("keep *"),
#                                  fileName = cms.untracked.string('dump.root')
#                                  )
#
#process.out_step = cms.EndPath(process.output)
