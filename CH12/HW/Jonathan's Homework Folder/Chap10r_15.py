# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:08:21 2016

@author: kiaph
"""

from graphics import *
from projectile import Projectile


class Tracker:
    def __init__(self, window, objToTrack):
        self.winx = window
        #self.winx.draw(winx)
        self.obj = objToTrack
        self.obj.getX() = xpos
        self.obj.getY() = ypos
        
    
   
   
    def updater(self):
        #draws circle
        obj.getX() = xpos
        obj.getY() = ypos
        center = Point(xpos,ypos)
        self.circ = Circle(center,3)
        self.circ.fillOutline("red")
        self.circ.draw(winx)
     
        
        # window is a graphWin and objToTrack is an object whose
        #    position is to be show in the window. objToTrack is 
        #    an object that has getX() and getY() methods 
        #    that report its current position
        #
        
        # Creates a Tracker object and draws a circle in a window 
        #    at the current position of objToTrack.
        # 
        #   def update():
        #       moves the circle in the window to the current position   
        #           of the object being tracked
        #
        
        
        
        
        
        
        '''def window(self,window):
            self.win = GraphWin(window,420,420)
            self.win.setBackground("white")
            
            self.win.getMouse()
            self.win.close()'''
        
         #this was my first attempt.
        
        '''def objToTrack(self,x,y):
          
                
        def update(self,x,y):
            self.xpos = x
            self.ypos = y
            self.Circle(Point(xpos,ypos),3) = cir
            self.cir.fillOutline("red")
            self.cir.draw(win)'''
            
            
    #def objToTrack():
        
        

