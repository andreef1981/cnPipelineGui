#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:56:19 2019

@author: Andre Fehlmann (afehlmann@nso.edu)
"""
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np

Array = np.random.rand(100, 100)
grid_points = 100
fig_mpl, ax = plt.subplots(figsize = (10, 10), facecolor = 'white')

line = ax.imshow(Array, cmap = 'hot')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.05)
caxb = divider.append_axes("bottom", size = "10%", pad = 0.05)
caxl = divider.append_axes("left", size = "10%", pad = 0.05)

bar = fig_mpl.colorbar(line, cax = cax, orientation = 'vertical') 
ax.axhline(grid_points/2)
ax.axvline(grid_points/2)      

X = np.linspace(0, grid_points - 1, grid_points)      
projb, = caxb.plot(X, Array[int(grid_points/2)], color = 'red')
projl, = caxl.plot(Array[:, int(grid_points/2)], X, color = 'red')

caxb.set_ylim(-0.1*np.max(Array), 1.1*np.max(Array))
caxb.set_xlim(0, grid_points - 1)
caxl.set_xlim(-0.1*np.max(Array), 1.1*np.max(Array))
caxl.set_ylim(0, grid_points - 1)

ax.set_xticks([])
ax.set_yticks([])
caxb.set_xticks([])
caxl.set_yticks([])
caxb.set_yticks([np.min(Array), np.max(Array)])
caxl.set_xticks([np.min(Array), np.max(Array)])
caxb.yaxis.tick_right()

for tick in caxl.get_xticklabels():
    tick.set_rotation(-90)

caxb.grid(color = 'black', marker = 8)
caxl.grid(color = 'black', marker = 8)

fig_mpl.subplots_adjust(wspace = 0)
fig_mpl.tight_layout()