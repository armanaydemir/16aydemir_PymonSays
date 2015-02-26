#!/usr/bin/env python2.7
# beep.py
# 8-note, .5-second beep synth class
# Arman Aydemir
# 03/30/2014

import pygame
from pygame import *
import sys

#class for importing beeps
class Beeps:
	scale = []
	
	#initializes the scale
	def __init__(self):
		self.scale.append(pygame.mixer.Sound("snd/C_low.wav"))
		self.scale.append(pygame.mixer.Sound("snd/D.wav"))
		self.scale.append(pygame.mixer.Sound("snd/E.wav"))
		self.scale.append(pygame.mixer.Sound("snd/F.wav"))
		self.scale.append(pygame.mixer.Sound("snd/G.wav"))
		self.scale.append(pygame.mixer.Sound("snd/A.wav"))
		self.scale.append(pygame.mixer.Sound("snd/B.wav"))
		self.scale.append(pygame.mixer.Sound("snd/C_hi.wav"))
		
	#gets sound from the list
	def get_sound(self, index):
		try:
			return self.scale[index]
		except:
			print('Index out of bounds exception error: index=' + str(index) + ' Min index=0 Max index=7')
			return None		