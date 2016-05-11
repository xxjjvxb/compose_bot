import midi
import glob
import os
from midi.utils import midiread, midiwrite

import random as rd

import theano
import theano.tensor as T

import numpy

import cPickle as pkl

if __name__ == "__main__":
	
	count = pkl.load(open("bi-gram-count.dat","rb")) #load data from file
		
	length = 200;
	time = 0;
	
	generated = numpy.zeros((length, 88)) 
	
	while True:
		time = time + 1
		
		if time == length:
			break
			
			
		sumOfZero = 0
		sumOfOne = 0
		
		for note in range(88) : 
			for noteFrom in range(88) : 
				valueFrom = int (generated[time-1][noteFrom])
				
				sumOfZero = sumOfZero + count[note][0][noteFrom][valueFrom]
				sumOfOne = sumOfOne + count[note][1][noteFrom][valueFrom]
			
			ratio = sumOfOne / sumOfZero
			
			
			if (ratio/5) > rd.random(): # using orgin ratio directly brings too many notes
				generated[time][note] = 1
	
		#print sum(generated[time])
		
	
	midiwrite("output-bi.mid", generated)
	
	
	
	
	
	
