#!/usr/bin/env python2.7
# pyButton.py
# makes the buttons of py
# Arman Aydemir
# March, 30 2014


import pygame
from pygame import *

#color constants
RED = (255,0,0)
LIGHTRED = (255,102,102)
GREEN = (0,255,0)
LIGHTGREEN = (102,255,102)
BLUE = (0,0,255)
LIGHTBLUE = (51,153,255)
YELLOW = (255,255,0)
LIGHTYELLOW = (255,255,153)

#class for constructing buttons
class PyButton:
	color = None
	shape = None
	sound = None
	
	#initializes variables
	def __init__(self, color, shape, sound):
		self.color = color
		self.shape = shape
		self.sound = sound
		
	#flashes button
	def flash(self):
		if self.color == RED:
			self.color = LIGHTRED	#red
		elif self.color == GREEN:
			self.color = LIGHTGREEN	#green
		elif self.color == BLUE:
			self.color = LIGHTBLUE		#blue
		elif self.color == YELLOW:
			self.color = LIGHTYELLOW	#yellow

	#resets what flash does
	def reset(self):
		if self.color == LIGHTRED:
			self.color	= RED	#red
		elif self.color == LIGHTGREEN:
			self.color	= GREEN		#green
		elif self.color == LIGHTBLUE:
			self.color = BLUE	#blue
		elif self.color == LIGHTYELLOW:
			self.color = YELLOW	#yellow
			
	#checks to see if constructed button contains click
	def contains_click(self, point):
		return self.shape.collidepoint(point)
	
	#plays sound
	def play_sound(self):
		self.sound.play()