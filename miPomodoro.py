#!/usr/bin/env python
# Unity indicator for evolution-less clock and date display
# author: phil ayres
# 24 Oct 2011
 
import gtk
import appindicator
import sys, math, datetime

class Pomodoro:

    DEFAULT_POMODORO_TIME = 25*60 # seconds for a pomodoro

    def __init__(self):
    	self.REMAINING_POMODORO_TIME = self.DEFAULT_POMODORO_TIME + 1
    	self.ind = appindicator.Indicator("new-pomodoro-indicator",
                                         "clock",
                                         appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
    	self.menu = gtk.Menu()
        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def quit(self, widget):
        sys.exit(0)

    	
    def start(self):
       	self.updatePomodoroTime()
       	gtk.timeout_add(1000, self.updatePomodoroTime)
       	gtk.main()


    def updatePomodoroTime(self):
    	ret = (self.REMAINING_POMODORO_TIME != 0) 
    	if self.REMAINING_POMODORO_TIME != 0:
    		self.REMAINING_POMODORO_TIME -= 1
    		self.printFormattedTime(self.REMAINING_POMODORO_TIME)
		return ret
    
    def printFormattedTime(self, remainingTime):
    	time2print = str(datetime.timedelta(seconds = remainingTime))
    	self.ind.set_label(time2print[2:])

if __name__ == "__main__":		

	pomodoro = Pomodoro()
	pomodoro.start()
