#!/usr/bin/env python2.7
# pymonSays.py
# test out a cool pygame loop and a button
# 03.30.2014

#imports everything necessary
import random
from random import *
import pygame
from pygame import *
import sys
from beeps import Beeps
from pyButton import PyButton
from threading import Thread, Event, Timer
import time

print "Terminal used only for Debug"
        
#class for buttons
#==============
class Button:
	screen = None
	pyButtons = []
	beeps = None
	
	#initializes the class variables and the four buttons
	#==================
	def __init__(self):
		mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
		pygame.mixer.get_init()
		pygame.init()
		self.beeps = Beeps()
		# the process below is called CONSTRUCTION
		self.pyButtons.append(PyButton((0,255,0), Rect(100,100,250,250),
			self.beeps.get_sound(0)))
		self.pyButtons.append(PyButton((255,0,0), Rect(450,100,250,250),
			self.beeps.get_sound(2)))
		self.pyButtons.append(PyButton((0,0,255), Rect(450,450,250,250),
			self.beeps.get_sound(1)))
		self.pyButtons.append(PyButton((255,255,0), Rect(100,450,250,250),
			self.beeps.get_sound(3)))
		self.screen = pygame.display.set_mode((800, 800), 0, 0)
		pygame.display.set_caption('*** Pymon Says ***')

	#flashes the button inputed for a selected about of time
	#============================
	def flasher(self, btn, delay):
		btn.flash()
		pygame.draw.rect(self.screen, btn.color, btn.shape)
		pygame.display.flip()
		btn.play_sound()
		pygame.time.delay(delay)
		btn.reset()
		pygame.draw.rect(self.screen, btn.color, btn.shape)
		pygame.display.flip()
		
	#redraws the buttons
	#=================
	def redraw(self):
		self.screen.fill((0,0,0))
		for btn in self.pyButtons:
			pygame.draw.rect(self.screen, btn.color, btn.shape)

#main function
#===========
def main():
	#sets veriables for the main game loop
	#=========
	order = []
	order.append(randint(0,3))
	app = Button()
	app.screen.fill((0,0,0))
	shortorder = []
	keys = [K_q, K_w, K_s, K_a]
	
	#pre-game message
	#==================================
	message = pygame.font.Font(None, 40)
	msg = pygame.font.Font(None, 32)
	label = message.render("Get Ready to play!",1,(255,255,255))
	hint = msg.render("You can use  the keys Q, W, A, and S to select buttons",1,(255,255,255))
	app.screen.blit(label, (285,400))
	app.screen.blit(hint, (150,600))
	pygame.display.flip()
	pygame.time.delay(2000)
	app.screen.fill((0,0,0))
	
	#main game loop - game is played entirely within this loop
	#============
	while True:
		flashDelay = 325
		lost = False
		click = True
		
		#draws the buttons and flashes buttons along with changing the delay
		#======================
		app.redraw()
		pygame.display.flip()
		pygame.time.delay(750)
		if flashDelay > 50:
			flashDelay -= 15
		for i in order:
			btn = app.pyButtons[i]
			app.flasher(btn, flashDelay)
			print str(i)
		print "-----"
		shortorder = []
		
		#makes it so the game disregards any events during the beeps unless it was to quit
		#===============================
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				
		#gets current time and sets start to that (for timer)	
		start = time.clock()
		
		#loop that runs while comp is awaiting user's input
		#============
		while click:
			
			#checks amount of time that has passes since start was set to current time
			#==============================
			elapsed = time.clock() - start
			
			#if it is more than twenty seconds you lose the game
			#==================
			if elapsed >= 20:
				lost = True
				app.redraw()
			 	label = msg.render("You took too long",1,(255,255,255))
			 	app.screen.blit(label, (325,750))
			 	pygame.display.flip()
			 	break
			 	
			#if it is more than ten seconds it tells you to wake up
			#===================
			elif elapsed >= 10:
				label = message.render("Wake up!",1,(255,255,255))
			 	app.screen.blit(label, (335,400))
			 	pygame.display.flip()
			 	
			for event in pygame.event.get():
			
				#ways to quit game
				#=====================
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
						
					#lets user use q, w , s, and a to select buttons (extra)
					#=====================
					for i in keys:
						if event.key == i:
							btn = app.pyButtons[keys.index(i)]
							app.flasher(btn,300)
							shortorder.append(keys.index(i))
							app.redraw()
							
							#resets the timer because of user input
							#=====================
							start = time.clock()
							
				#process the click and makes clicked on button flash
				#===================================
				elif event.type == MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					for btn in app.pyButtons:
						if btn.contains_click(pos):
							position = app.pyButtons.index(btn)
							app.flasher(btn, 300)
							shortorder.append(position)
							app.redraw()
							
							#resets the timer because of user input
							#=====================
							start = time.clock()
							
			
			#processes the selection to find whether or not it is correct
			#========================
			if shortorder == order:
				click = False
				break
			else:
				if shortorder != order[0:len(shortorder)]:
					click = False
					lost = True
					
		#adds another random button to the order and makes sure it doesn't add the same one three times in a row
		#=======================
		randnum = randint(0,3)
		while randnum == order[len(order)-1] and randnum == order[len(order)-2]:
			randnum = randint(0,3)
		order.append(randnum)
		
		#draws buttons again
		#========================
		for btn in app.pyButtons:
			pygame.draw.rect(app.screen, btn.color, btn.shape)
		pygame.display.flip()
		
		#what happens if you lose
		#============
		if lost:
			print "You lost"
			if len(order)-2 == 1:
				label = message.render("You lasted "  + str(len(order)-2) + " round",1,(255,255,255))
			else:
				label = message.render("You lasted "  + str(len(order)-2) + " rounds",1,(255,255,255))
			app.screen.blit(label, (270,400))
			pygame.display.flip()
			pygame.time.delay(1500)
			app.screen.fill((0,0,0))
			pygame.time.delay(1100)
			for btn in app.pyButtons:
				pygame.draw.rect(app.screen, btn.color, btn.shape)
				pygame.display.flip()
				pygame.time.delay(500)
			order = []
			flashDelay = 325
			order.append(randnum)
main()