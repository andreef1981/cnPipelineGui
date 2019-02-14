#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:02:16 2019

@author: Andre Fehlmann (afehlmann@nso.edu)
"""
from mpl_toolkits.axes_grid1 import make_axes_locatable
# import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.widgets import Cursor

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.widgets import Button


 #%%       
class cnImage:
  def __init__(self, array):
    self.array = array
    self.xSize = self.array.shape[1]
    self.ySize = self.array.shape[0]
    self.cursorLocation = [50,50]
    
    self.fig, self.ax = plt.subplots()
    line = self.ax.imshow(self.array,aspect='equal',interpolation='none')
    divider = make_axes_locatable(self.ax)
    self.cax = divider.append_axes("right", size = "5%", pad = 0.05)
    self.caxb = divider.append_axes("bottom", size = "10%", pad = 0.05)
    self.caxl = divider.append_axes("left", size = "10%", pad = 0.05)
    self.caxl.xaxis.tick_top()
    
    bar = self.fig.colorbar(line, cax = self.cax, orientation = 'vertical')
    
    self.enterEvent = self.fig.canvas.mpl_connect('axes_enter_event', self.on_enter)
    self.leaveEvent = self.fig.canvas.mpl_connect('axes_leave_event', self.on_leave)
    self.moveEvent = self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
    self.cursor = Cursor(self.ax, useblit=False, color='red', linewidth=2)
    
    self.fig.subplots_adjust(wspace = 0)
    self.fig.tight_layout()
    axprev = plt.axes([0.7, 0.85, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.85, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    plt.show()
    
  def on_enter(self, event):
    # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       ('double' if event.dblclick else 'single', event.button,
    #        event.x, event.y, event.xdata, event.ydata))
    # Set useblit=True on most backends for enhanced performance.
    
    self.cursor.visible = True
    
  def on_leave(self, event):
  
    # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       ('double' if event.dblclick else 'single', event.button,
    #        event.x, event.y, event.xdata, event.ydata))
    # Set useblit=True on most backends for enhanced performance.
    self.cursor.visible=False
    
  def on_move(self, event):
    
    if (event.xdata != None) and (event.ydata != None):
      X = np.arange(self.xSize) 
      Y = np.arange(self.ySize) 
      self.caxb.clear()
      projb, = self.caxb.plot(X, self.array[int(event.ydata),:], color = 'red')
      self.caxb.set_ylim(np.min(self.array[int(event.ydata),:]), np.max(self.array[int(event.ydata),:]))
      self.caxb.set_xlim(0, self.xSize)
      self.caxl.clear()
      projl, = self.caxl.plot(self.array[int(event.xdata),:],Y, color = 'red')
      self.caxl.set_xlim(np.min(self.array[int(event.xdata),:]), np.max(self.array[int(event.xdata),:]))
      self.caxl.set_ylim(0, self.ySize)
      # self.caxl.xaxis.tick_top()
      plt.sca(self.caxl)
      plt.xticks(rotation=90)
      plt.sca(self.cax)
  

    
    # self.ax.set_xticks([])
    # self.ax.set_yticks([])
    # caxb.set_xticks([])
    # caxl.set_yticks([])
    # caxb.set_yticks([np.min(self.array), np.max(self.array)])
    # caxl.set_xticks([np.min(self.array), np.max(self.array)])
    # caxb.yaxis.tick_right()
    
    # for tick in caxl.get_xticklabels():
    #     tick.set_rotation(-90)
    
    # caxb.grid(color = 'black', marker = 8)
    # caxl.grid(color = 'black', marker = 8)
    
    # 
    

array = np.random.rand(2048, 2048)
cnImage(array)

#%% 
#class Window(QtWidgets.QDialog):
#   def __init__(self,array, parent=None):
#     super(Window, self).__init__(parent)
#     self.array = array
#     self.figure = plt.figure(facecolor='white')
#     self.canvas = FigureCanvas(self.figure)
#     self.toolbar = NavigationToolbar(self.canvas, self)
#     # set the layout
#     layout = QtWidgets.QVBoxLayout()
#     layout.addWidget(self.toolbar)
#     layout.addWidget(self.canvas)
    
#     self.setLayout(layout)

#     ''' plot some random stuff '''
#     ax = self.figure.add_subplot(111)
#     # self.ax = ax
#     ax.imshow(array)
#     #ax.plot(np.arange(10))
#     # Set cursor        
#     self.cursor = Cursor(ax, useblit=False, color='black', linewidth=10)

#     ############## The added part: #############
#     def onclick(event):
#         self.cursor.onmove(event)
#     self.canvas.mpl_connect('button_press_event', onclick)
#     ############################################
#     plt.show()
#     self.canvas.draw()

    
# array = np.random.rand(100, 100)
# # Window(array)
# if __name__ == '__main__':
#   app = QtWidgets.QApplication(sys.argv)
  
#   main = Window(array)
#   main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
#   main.show()
  
#   sys.exit(app.exec_())