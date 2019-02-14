#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:41:46 2019

@author: Andre Fehlmann (afehlmann@nso.edu)
"""

from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#FFFFCC')

# x, y = 4*(np.random.rand(2, 100) - .5)
# ax.plot(x, y, 'o')
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
ax.imshow(np.zeros([10,10]))

# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import MultiCursor

# t = np.arange(0.0, 2.0, 0.01)
# s1 = np.sin(2*np.pi*t)
# s2 = np.sin(4*np.pi*t)
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax1.plot(t, s1)


# ax2 = fig.add_subplot(212, sharex=ax1)
# ax2.plot(t, s2)

# multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)