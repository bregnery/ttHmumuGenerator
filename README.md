ttHmumuGenerator
================

This program creates a ttHmumu 13 TeV Monte Carlo sample

Instructions
============

A UF HPC account is highly recommended in order to use this program.

This program has been tested with CMSSW_7_4_2. To use this program, obtain this CMSSW release and move into the source directory.

    cmsrel CMSSW_7_4_2
    cd CMSSW_7_4_2
    cd src
    cmsenv
  
Then, clone this git repository and compile CMSSW

    git clone https://github.com/bregnery/ttHmumuGenerator.git
    scram b
    cmsenv
  
Next, move into ttHmumuGenerator.
