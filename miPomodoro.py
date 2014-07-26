#!/usr/bin/env python
# Unity indicator for evolution-less clock and date display
# author: phil ayres
# 24 Oct 2011
 
import gobject
import gtk
import appindicator
import os, sys



class Pomodoro:


    DEFAULT_POMODORO_TIME = 30 # seconds for a pomodoro

    def __init__(self):
    	self.REMAINING_POMODORO_TIME = self.DEFAULT_POMODORO_TIME

    def start(self):
       	self.updatePomodoroTime()
       	gtk.timeout_add(1000, self.updatePomodoroTime)
       	gtk.main()


    def updatePomodoroTime(self):
    	ret = (self.REMAINING_POMODORO_TIME != 0) 
    	if self.REMAINING_POMODORO_TIME != 0:
    		self.REMAINING_POMODORO_TIME -= 1
    		print(self.REMAINING_POMODORO_TIME)
		
		return ret    		

    def stop():
    	pass

    def setPomodoroTime(pomodoroTime):
    	self.DEFAULT_POMODORO_TIME = pomodoroTime*60*1000


if __name__ == "__main__":		

	pomodoro = Pomodoro()
	pomodoro.start()
