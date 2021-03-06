import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectorsAllAlgos_cff import *
from JetMETCorrections.Configuration.CorrectedJetProducers_cff import *

# L1 Correction Producers
ak7CaloJetsL1 = ak4CaloJetsL1.clone( src = 'ak7CaloJets' )
kt4CaloJetsL1 = ak4CaloJetsL1.clone( src = 'kt4CaloJets' )
kt6CaloJetsL1 = ak4CaloJetsL1.clone( src = 'kt6CaloJets' )
ic5CaloJetsL1 = ak4CaloJetsL1.clone( src = 'ic5CaloJets' )

ak1PFJetsL1 = ak4PFJetsL1.clone( src = 'ak1PFJets' )
ak1PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak1PFCHSJets' )
ak2PFJetsL1 = ak4PFJetsL1.clone( src = 'ak2PFJets' )
ak2PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak2PFCHSJets' )
ak3PFJetsL1 = ak4PFJetsL1.clone( src = 'ak3PFJets' )
ak3PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak3PFCHSJets' )
ak5PFJetsL1 = ak4PFJetsL1.clone( src = 'ak5PFJets' )
ak5PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak5PFCHSJets' )
ak6PFJetsL1 = ak4PFJetsL1.clone( src = 'ak6PFJets' )
ak6PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak6PFCHSJets' )
ak7PFJetsL1 = ak4PFJetsL1.clone( src = 'ak7PFJets' )
ak7PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak7PFCHSJets' )
ak8PFJetsL1 = ak4PFJetsL1.clone( src = 'ak8PFJets' )
ak8PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak8PFCHSJets' )
ak9PFJetsL1 = ak4PFJetsL1.clone( src = 'ak9PFJets' )
ak9PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak9PFCHSJets' )
ak10PFJetsL1 = ak4PFJetsL1.clone( src = 'ak10PFJets' )
ak10PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak10PFCHSJets' )
kt4PFJetsL1 = ak4PFJetsL1.clone( src = 'kt4PFJets' )
kt6PFJetsL1 = ak4PFJetsL1.clone( src = 'kt6PFJets' )
ic5PFJetsL1 = ak4PFJetsL1.clone( src = 'ic5PFJets' )


# L2L3 Correction Producers
ak7CaloJetsL2 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2RelativeCorrector'])
kt4CaloJetsL2 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2RelativeCorrector'])
kt6CaloJetsL2 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2RelativeCorrector'])
ic5CaloJetsL2 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2RelativeCorrector'])

ak1PFJetsL2 = ak1PFJetsL1.clone(correctors = ['ak1PFL2RelativeCorrector'])
ak1PFCHSJetsL2 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL2RelativeCorrector'])
ak2PFJetsL2 = ak2PFJetsL1.clone(correctors = ['ak2PFL2RelativeCorrector'])
ak2PFCHSJetsL2 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL2RelativeCorrector'])
ak3PFJetsL2 = ak3PFJetsL1.clone(correctors = ['ak3PFL2RelativeCorrector'])
ak3PFCHSJetsL2 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL2RelativeCorrector'])
ak5PFJetsL2 = ak5PFJetsL1.clone(correctors = ['ak5PFL2RelativeCorrector'])
ak5PFCHSJetsL2 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL2RelativeCorrector'])
ak6PFJetsL2 = ak6PFJetsL1.clone(correctors = ['ak6PFL2RelativeCorrector'])
ak6PFCHSJetsL2 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL2RelativeCorrector'])
ak7PFJetsL2 = ak7PFJetsL1.clone(correctors = ['ak7PFL2RelativeCorrector'])
ak7PFCHSJetsL2 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL2RelativeCorrector'])
ak8PFJetsL2 = ak8PFJetsL1.clone(correctors = ['ak8PFL2RelativeCorrector'])
ak8PFCHSJetsL2 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL2RelativeCorrector'])
ak9PFJetsL2 = ak9PFJetsL1.clone(correctors = ['ak9PFL2RelativeCorrector'])
ak9PFCHSJetsL2 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL2RelativeCorrector'])
ak10PFJetsL2 = ak10PFJetsL1.clone(correctors = ['ak10PFL2RelativeCorrector'])
ak10PFCHSJetsL2 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL2RelativeCorrector'])
kt4PFJetsL2 = kt4PFJetsL1.clone(correctors = ['kt4PFL2RelativeCorrector'])
kt6PFJetsL2 = kt6PFJetsL1.clone(correctors = ['kt6PFL2RelativeCorrector'])
ic5PFJetsL2 = ic5PFJetsL1.clone(correctors = ['ic5PFL2RelativeCorrector'])

ak4JPTJetsL2 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL2RelativeCorrector'])
ak4TrackJetsL2 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL2RelativeCorrector'])

# L2L3 Correction Producers
ak7CaloJetsL2L3 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2L3Corrector'])
kt4CaloJetsL2L3 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2L3Corrector'])
kt6CaloJetsL2L3 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2L3Corrector'])
ic5CaloJetsL2L3 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2L3Corrector'])

ak1PFJetsL2L3 = ak1PFJetsL1.clone(correctors = ['ak1PFL2L3Corrector'])
ak1PFCHSJetsL2L3 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL2L3Corrector'])
ak2PFJetsL2L3 = ak2PFJetsL1.clone(correctors = ['ak2PFL2L3Corrector'])
ak2PFCHSJetsL2L3 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL2L3Corrector'])
ak3PFJetsL2L3 = ak3PFJetsL1.clone(correctors = ['ak3PFL2L3Corrector'])
ak3PFCHSJetsL2L3 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL2L3Corrector'])
ak5PFJetsL2L3 = ak5PFJetsL1.clone(correctors = ['ak5PFL2L3Corrector'])
ak5PFCHSJetsL2L3 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL2L3Corrector'])
ak6PFJetsL2L3 = ak6PFJetsL1.clone(correctors = ['ak6PFL2L3Corrector'])
ak6PFCHSJetsL2L3 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL2L3Corrector'])
ak7PFJetsL2L3 = ak7PFJetsL1.clone(correctors = ['ak7PFL2L3Corrector'])
ak7PFCHSJetsL2L3 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL2L3Corrector'])
ak8PFJetsL2L3 = ak8PFJetsL1.clone(correctors = ['ak8PFL2L3Corrector'])
ak8PFCHSJetsL2L3 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL2L3Corrector'])
ak9PFJetsL2L3 = ak9PFJetsL1.clone(correctors = ['ak9PFL2L3Corrector'])
ak9PFCHSJetsL2L3 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL2L3Corrector'])
ak10PFJetsL2L3 = ak10PFJetsL1.clone(correctors = ['ak10PFL2L3Corrector'])
ak10PFCHSJetsL2L3 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL2L3Corrector'])
kt4PFJetsL2L3 = kt4PFJetsL1.clone(correctors = ['kt4PFL2L3Corrector'])
kt6PFJetsL2L3 = kt6PFJetsL1.clone(correctors = ['kt6PFL2L3Corrector'])
ic5PFJetsL2L3 = ic5PFJetsL1.clone(correctors = ['ic5PFL2L3Corrector'])

ak4JPTJetsL2L3 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL2L3Corrector'])
ak4TrackJetsL2L3 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL2L3Corrector'])

# L1L2L3 Correction Producers
ak7CaloJetsL1L2L3 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL1L2L3Corrector'])
kt4CaloJetsL1L2L3 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL1L2L3Corrector'])
kt6CaloJetsL1L2L3 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL1L2L3Corrector'])
ic5CaloJetsL1L2L3 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL1L2L3Corrector'])

ak1PFJetsL1L2L3 = ak1PFJetsL1.clone(correctors = ['ak1PFL1L2L3Corrector'])
ak1PFCHSJetsL1L2L3 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL1L2L3Corrector'])
ak2PFJetsL1L2L3 = ak2PFJetsL1.clone(correctors = ['ak2PFL1L2L3Corrector'])
ak2PFCHSJetsL1L2L3 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL1L2L3Corrector'])
ak3PFJetsL1L2L3 = ak3PFJetsL1.clone(correctors = ['ak3PFL1L2L3Corrector'])
ak3PFCHSJetsL1L2L3 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL1L2L3Corrector'])
ak5PFJetsL1L2L3 = ak5PFJetsL1.clone(correctors = ['ak5PFL1L2L3Corrector'])
ak5PFCHSJetsL1L2L3 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL1L2L3Corrector'])
ak6PFJetsL1L2L3 = ak6PFJetsL1.clone(correctors = ['ak6PFL1L2L3Corrector'])
ak6PFCHSJetsL1L2L3 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL1L2L3Corrector'])
ak7PFJetsL1L2L3 = ak7PFJetsL1.clone(correctors = ['ak7PFL1L2L3Corrector'])
ak7PFCHSJetsL1L2L3 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL1L2L3Corrector'])
ak8PFJetsL1L2L3 = ak8PFJetsL1.clone(correctors = ['ak8PFL1L2L3Corrector'])
ak8PFCHSJetsL1L2L3 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL1L2L3Corrector'])
ak9PFJetsL1L2L3 = ak9PFJetsL1.clone(correctors = ['ak9PFL1L2L3Corrector'])
ak9PFCHSJetsL1L2L3 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL1L2L3Corrector'])
ak10PFJetsL1L2L3 = ak10PFJetsL1.clone(correctors = ['ak10PFL1L2L3Corrector'])
ak10PFCHSJetsL1L2L3 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL1L2L3Corrector'])
kt4PFJetsL1L2L3 = kt4PFJetsL1.clone(correctors = ['kt4PFL1L2L3Corrector'])
kt6PFJetsL1L2L3 = kt6PFJetsL1.clone(correctors = ['kt6PFL1L2L3Corrector'])
ic5PFJetsL1L2L3 = ic5PFJetsL1.clone(correctors = ['ic5PFL1L2L3Corrector'])

ak4JPTJetsL1L2L3 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL1L2L3Corrector'])
ak4TrackJetsL1L2L3 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL1L2L3Corrector'])

# L2L3L6 CORRECTION PRODUCERS
ak7CaloJetsL2L3L6 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2L3L6Corrector'])
kt4CaloJetsL2L3L6 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2L3L6Corrector'])
kt6CaloJetsL2L3L6 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2L3L6Corrector'])
ic5CaloJetsL2L3L6 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2L3L6Corrector'])

ak7PFJetsL2L3L6 = ak7PFJetsL1.clone(correctors = ['ak7PFL2L3L6Corrector'])
kt4PFJetsL2L3L6 = kt4PFJetsL1.clone(correctors = ['kt4PFL2L3L6Corrector'])
kt6PFJetsL2L3L6 = kt6PFJetsL1.clone(correctors = ['kt6PFL2L3L6Corrector'])
ic5PFJetsL2L3L6 = ic5PFJetsL1.clone(correctors = ['ic5PFL2L3L6Corrector'])


# L1L2L3L6 CORRECTION PRODUCERS
ak7CaloJetsL1L2L3L6 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL1L2L3L6Corrector'])
kt4CaloJetsL1L2L3L6 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL1L2L3L6Corrector'])
kt6CaloJetsL1L2L3L6 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL1L2L3L6Corrector'])
ic5CaloJetsL1L2L3L6 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL1L2L3L6Corrector'])

ak7PFJetsL1L2L3L6 = ak7PFJetsL1.clone(correctors = ['ak7PFL1L2L3L6Corrector'])
kt4PFJetsL1L2L3L6 = kt4PFJetsL1.clone(correctors = ['kt4PFL1L2L3L6Corrector'])
kt6PFJetsL1L2L3L6 = kt6PFJetsL1.clone(correctors = ['kt6PFL1L2L3L6Corrector'])
ic5PFJetsL1L2L3L6 = ic5PFJetsL1.clone(correctors = ['ic5PFL1L2L3L6Corrector'])
