# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/h2mu_tth_M125GeV_13TeV_cfi.py --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --pileup AVE_20_BX_25ns --conditions PHYS14_25_V1 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --magField 38T_PostLS1 --geometry Extended2015 --beamspot Realistic8TeVCollision --datatier GEN-SIM --mc --eventcontent AODSIM --python_filename h2mu_tth_M125GeV_13TeV_FULLSIM_cfg.py -n 10 --no_exec --fileout h2mu_tth_M125GeV_13TeV_pythia6_AODSIM_1.root
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)       #number of events to generate
)

# Input source
process.source = cms.Source("EmptySource")

outputFile=""
jobNum=""
def getVal(arg):
	i=0
	while i < len(arg) and arg[i] != "=": i+=1
	return arg[i+1:]

## loop over arguments
for i in range(1,len(sys.argv)):
	print "[arg "+str(i)+"] : ", sys.argv[i] 
	
	if "output" in sys.argv[i]:
		outputFile=getVal(sys.argv[i])
		#print "oHERE"
		
	if "job" in sys.argv[i] :
		jobNum=getVal(sys.argv[i])
		#print "jHERE"

print outputFile
print jobNum


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/h2mu_tth_M125GeV_13TeV_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string(outputFile),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/001CB469-A91E-E311-9BFE-0025907FD24A.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/009CB248-A81C-E311-ACD8-00259073E4F0.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/009F81D5-B21C-E311-966C-BCAEC50971D0.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00B5BB8C-A91E-E311-816A-782BCB1F5E6B.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00B8F676-BA1C-E311-BA87-0019B9CABFB6.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00DD7446-B51D-E311-B714-001E6739CEB1.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/021E1B53-101D-E311-886F-00145EDD7569.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/022A782D-A51C-E311-9856-80000048FE80.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/026FE678-BA1C-E311-BEF5-00D0680BF90A.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/02A10BDE-B21C-E311-AB59-00266CF327C0.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters'),
        processParameters = cms.vstring('MSEL=0             ! User defined processes', 
            'MSUB(121)=1        ! gg to ttH', 
            'MSUB(122)=1        ! qq to ttH', 
            'PMAS(25,1)= 125.   ! m_h', 
            'PMAS(6,1)= 172.6   ! mass of top quark', 
            'PMAS(23,1)= 91.187 ! mass of Z', 
            'PMAS(24,1)= 80.39  ! mass of W', 
            'MDME(210,1)=0      ! d               dbar', 
            'MDME(211,1)=0      ! u               ubar', 
            'MDME(212,1)=0      ! s               sbar', 
            'MDME(213,1)=0      ! c               cbar', 
            'MDME(214,1)=0      ! b               bbar', 
            'MDME(215,1)=0      ! t               tbar', 
            'MDME(216,1)=0      ! bp              bp bar', 
            'MDME(217,1)=0      ! tp              tp bar', 
            'MDME(218,1)=0      ! e-              e+', 
            'MDME(219,1)=1      ! mu-             mu+', 
            'MDME(220,1)=0      ! tau-            tau+', 
            'MDME(221,1)=0      ! taup -           taup +', 
            'MDME(222,1)=0      ! g               g', 
            'MDME(223,1)=0      ! gamma           gamma', 
            'MDME(224,1)=0      ! gamma           Z0', 
            'MDME(225,1)=0      ! Z0              Z0', 
            'MDME(226,1)=0      ! W+              W-', 
            'MDME(227,1)=0      ! ~chi_10         ~chi_10', 
            'MDME(228,1)=0      ! ~chi_20         ~chi_10', 
            'MDME(229,1)=0      ! ~chi_20         ~chi_20', 
            'MDME(230,1)=0      ! ~chi_30         ~chi_10', 
            'MDME(231,1)=0      ! ~chi_30         ~chi_20', 
            'MDME(232,1)=0      ! ~chi_30         ~chi_30', 
            'MDME(233,1)=0      ! ~chi_40         ~chi_10', 
            'MDME(234,1)=0      ! ~chi_40         ~chi_20', 
            'MDME(235,1)=0      ! ~chi_40         ~chi_40', 
            'MDME(237,1)=0      ! ~chi_1+         ~chi_1-', 
            'MDME(238,1)=0      ! ~chi_1+         ~chi_2-', 
            'MDME(239,1)=0      ! ~chi_2+         ~chi_1-', 
            'MDME(240,1)=0      ! ~chi_2+         ~chi_2-', 
            'MDME(241,1)=0      ! ~d_L            ~d_Lbar', 
            'MDME(242,1)=0      ! ~d_R            ~d_Rbar', 
            'MDME(243,1)=0      ! ~d_L            ~d_Rbar', 
            'MDME(244,1)=0      ! ~d_Lbar         ~d_R', 
            'MDME(245,1)=0      ! ~u_L            ~u_Lbar', 
            'MDME(246,1)=0      ! ~u_R            ~u_Rbar', 
            'MDME(247,1)=0      ! ~u_L            ~u_Rbar', 
            'MDME(248,1)=0      ! ~u_Lbar         ~u_R', 
            'MDME(249,1)=0      ! ~s_L            ~s_Lbar', 
            'MDME(250,1)=0      ! ~s_R            ~s_Rbar', 
            'MDME(251,1)=0      ! ~s_L            ~s_Rbar', 
            'MDME(252,1)=0      ! ~s_Lbar         ~s_R', 
            'MDME(253,1)=0      ! ~c_L            ~c_Lbar', 
            'MDME(254,1)=0      ! ~c_R            ~c_Rbar', 
            'MDME(255,1)=0      ! ~c_L            ~c_Rbar', 
            'MDME(256,1)=0      ! ~c_Lbar         ~c_R', 
            'MDME(257,1)=0      ! ~b_1            ~b_1bar', 
            'MDME(258,1)=0      ! ~b_2            ~b_2bar', 
            'MDME(259,1)=0      ! ~b_1            ~b_2bar', 
            'MDME(260,1)=0      ! ~b_1bar         ~b_2', 
            'MDME(261,1)=0      ! ~t_1            ~t_1bar', 
            'MDME(262,1)=0      ! ~t_2            ~t_2bar', 
            'MDME(263,1)=0      ! ~t_1            ~t_2bar', 
            'MDME(264,1)=0      ! ~t_1bar         ~t_2', 
            'MDME(265,1)=0      ! ~e_L-           ~e_L+', 
            'MDME(266,1)=0      ! ~e_R-           ~e_R+', 
            'MDME(267,1)=0      ! ~e_L-           ~e_R+', 
            'MDME(268,1)=0      ! ~e_L+           ~e_R-', 
            'MDME(269,1)=0      ! ~nu_eL          ~nu_eLbar', 
            'MDME(270,1)=0      ! ~nu_eR          ~nu_eRbar', 
            'MDME(271,1)=0      ! ~nu_eL          ~nu_eRbar', 
            'MDME(272,1)=0      ! ~nu_eLbar       ~nu_eR', 
            'MDME(273,1)=0      ! ~mu_L-          ~mu_L+', 
            'MDME(274,1)=0      ! ~mu_R-          ~mu_R+', 
            'MDME(275,1)=0      ! ~mu_L-          ~mu_R+', 
            'MDME(276,1)=0      ! ~mu_L+          ~mu_R-', 
            'MDME(277,1)=0      ! ~nu_muL         ~nu_muLbar', 
            'MDME(278,1)=0      ! ~nu_muR         ~nu_muRbar', 
            'MDME(279,1)=0      ! ~nu_muL         ~nu_muRbar', 
            'MDME(280,1)=0      ! ~nu_muLbar      ~nu_muR', 
            'MDME(281,1)=0      ! ~tau_1-         ~tau_1+', 
            'MDME(282,1)=0      ! ~tau_2-         ~tau_2+', 
            'MDME(283,1)=0      ! ~tau_1-         ~tau_2+', 
            'MDME(284,1)=0      ! ~tau_1+         ~tau_2-', 
            'MDME(285,1)=0      ! ~nu_tauL        ~nu_tauLbar', 
            'MDME(286,1)=0      ! ~nu_tauR        ~nu_tauRbar', 
            'MDME(287,1)=0      ! ~nu_tauL        ~nu_tauRbar', 
            'MDME(288,1)=0      ! ~nu_tauLbar     ~nu_tauR'),
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model')
    ),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(55000000000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

#genSeed = 9987 +1
genSeed = 9987 + int(jobNum)

# Generate event numbers
#process.source.firstRun = cms.untracked.uint32(1)
#process.generator.firstRun = cms.untracked.uint32(1)

process.source.firstRun = cms.untracked.uint32(int(jobNum))
process.generator.firstRun = cms.untracked.uint32(int(jobNum))


# Set the RNG seed for generation
process.RandomNumberGeneratorService.generator.initialSeed = genSeed

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

