import midi
import glob
import os
from midi.utils import midiread, midiwrite

import theano
import theano.tensor as T

import cPickle as pkl

probability = [ [ [[0.0]*2 for x in range(88)] for y in range(2)] for z in range(88) ]

def modeling_n_gram(n, files):
    
	assert len(files) > 0, 'Training set is empty!' \
					' (did you download the data files?)'
					
	for f in files:

		print 'parsing', f

		each = midiread(f).piano_roll.astype(theano.config.floatX)
		numNote = len(each[0])

		# each [ time ] [ note ]
	
		for timeSlice in range(n-1, len(each)):
			for noteDest in range(numNote):
				valueDest = int(each[timeSlice][noteDest])
				for noteFrom in range(numNote):
					valueFrom = int(each[timeSlice-1][noteFrom])
					
					#print noteDest,valueDest,noteFrom,valueFrom
					
					probability[noteDest][valueDest][noteFrom][valueFrom] \
						= probability[noteDest][valueDest][noteFrom][valueFrom] + 1.0
						
	print 'learning_done'
	
	pkl.dump(probability, open("bi-gram-count.dat", "wb"))
	
	print 'bi-gram-count.dat saved'
		

		
if __name__ == "__main__":

    re = os.path.join(os.path.split(os.path.dirname(__file__))[0],
                      'data', 'Nottingham', 'train', '*.mid')
    
    files = glob.glob(re)
    
    modeling_n_gram(2, files)
 
