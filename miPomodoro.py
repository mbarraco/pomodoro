#!/usr/bin/env python
# Unity indicator for evolution-less clock and date display
# author: phil ayres
# 24 Oct 2011
 
import gtk
import appindicator
import os, sys, math, datetime, pycanberra

class Pomodoro:

    DEFAULT_POMODORO_TIME = 4 # seconds for a pomodoro
    ALARM_SOUND = "alarm-clock-elapsed"

    def __init__(self):
    	self.canberra = pycanberra.Canberra()
    	



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

        self.set_time_item = gtk.MenuItem("Set pomodoro ")
        self.set_time_item.connect("activate", self.setTime)
        self.set_time_item.show()
        self.menu.append(self.set_time_item)

        self.stop_item = gtk.MenuItem("Stop")
        self.stop_item.connect("activate", self.stop)
        self.stop_item.show()
        self.menu.append(self.stop_item)

        self.start_item = gtk.MenuItem("Start")
        self.start_item.connect("activate", self.start)
        self.start_item.show()
        self.menu.append(self.start_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def quit(self, widget):
        sys.exit(0)

    	
    def start(self, widget):
       	self.updatePomodoroTime()
       	self.updateTag = gtk.timeout_add(1000, self.updatePomodoroTime)
       	gtk.main()

    def stop(self, widget):
    	gtk.timeout_remove(self.updateTag)
    	self.REMAINING_POMODORO_TIME = self.DEFAULT_POMODORO_TIME
    	self.printFormattedTime(self.REMAINING_POMODORO_TIME)
    	return True

    def updatePomodoroTime(self):
    	ret = (self.REMAINING_POMODORO_TIME != 0) 
    	if self.REMAINING_POMODORO_TIME != 0:
    		self.REMAINING_POMODORO_TIME -= 1
    	else:
    		self.canberra.easy_play_sync(self.ALARM_SOUND)
    		self.canberra.destroy()
    	self.printFormattedTime(self.REMAINING_POMODORO_TIME)
    	return ret
    
    def printFormattedTime(self, remainingTime):
    	time2print = str(datetime.timedelta(seconds = remainingTime))
    	self.ind.set_label(time2print[2:])

    def setTime(self, widget):
    	return True

if __name__ == "__main__":		

	pomodoro = Pomodoro()
	pomodoro.start(False)
