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
	
	print("reading data...")
	count = pkl.load(open("tri-gram-count.dat","rb"))
			
	length = 50; # length of music
	time = 1;
	
	generated = numpy.zeros((length, 88))
	
	'''## random initial
	for x in range(88):
		if (rd.random() > 0.90) :
			generated[time][x] = 1
	## '''
			
	# print max(max(max(max(max(count)))))
	
	while True:
		time = time + 1
		print(time,length)
		
		if time == length:
			break
			
			
		sumOfZero = 0
		sumOfOne = 0
		
		for note in range(88) : 
			for noteFrom in range(88) : 		
				valueFrom = int (generated[time-1][noteFrom])		
				
				for notePreFrom in range(88) : 
					valuePreFrom = int (generated[time-2][notePreFrom])		
					
					sumOfZero = sumOfZero + count[note][0][noteFrom][valueFrom][notePreFrom][valuePreFrom]
					sumOfOne = sumOfOne + count[note][1][noteFrom][valueFrom][notePreFrom][valuePreFrom]
			
			ratio = sumOfOne / sumOfZero
			
			# print ratio
			
			if (ratio/4) > rd.random(): #  using orgin ratio directly brings too many notes
				generated[time][note] = 1 # 
	
		# print sum(generated[time]) #print number of pressed note
		
	
	midiwrite("output-tri.mid", generated) # fileout
	
	
	
	
	
