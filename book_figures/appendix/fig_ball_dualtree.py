"""
Ball Dual-tree Diagram
----------------------
"""
# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general

import numpy as np
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

fig = plt.figure(figsize=(5, 2.5))
fig.subplots_adjust(left=0.05, right=0.95,
                    bottom=0.05, top=0.95)

#------------------------------------------------------------
ax = fig.add_subplot(111, xticks=[], yticks=[], aspect='equal')

Qx = np.array([[-0.3, -0.5, -0.7, -0.35, -0.58, -0.33],
               [0.4, 0.36, 0.68, 0.44, 0.77, 0.65]])

Rx = np.array([[0.24, 0.63, 0.7, 0.35, 0.58, 0.33],
               [0.34, 0.36, 0.68, 0.44, 0.78, 0.65]])

ax.plot([-0.5, 0.5], [0.5, 0.5], 'kx', ms=8)
ax.scatter(Qx[0], Qx[1], c='r', s=30)
ax.scatter(Rx[0], Rx[1], c='b', s=30)

ax.add_patch(plt.Circle((-0.5, 0.5), 0.3, fc='none', lw=2))
ax.add_patch(plt.Circle((0.5, 0.5), 0.35, fc='none', lw=2))

ax.arrow(-0.5, 0.5, -0.16, 0.26, width=0.01, lw=0, color='gray',
         length_includes_head=True, zorder=1)

ax.arrow(0.5, 0.5, 0.19, 0.29, width=0.01, lw=0, color='gray',
         length_includes_head=True, zorder=1)

ax.text(-0.8, 0.7, r'$Q$', ha='left', va='bottom', fontsize=12)
ax.text(0.8, 0.7, r'$R$', ha='left', va='bottom', fontsize=12)

ax.text(-0.55, 0.6, r'$r_Q$', ha='left', va='bottom', fontsize=12)
ax.text(0.5, 0.65, r'$r_R$', ha='left', va='bottom', fontsize=12)

ax.text(-0.5, 0.48, r'$\vec{\mu}_Q$', ha='left', va='top', fontsize=12)
ax.text(0.5, 0.48, r'$\vec{\mu}_R$', ha='left', va='top', fontsize=12)

ax.text(0, -0.08, r'$D^l(Q, R) = |\vec{\mu}_Q - \vec{\mu}_R| - r_Q - r_R$',
        va='bottom', ha='center', fontsize=12)
ax.text(0, 0.02, r'$D^u(Q, R) = |\vec{\mu}_Q - \vec{\mu}_R| + r_Q + r_R$',
        va='bottom', ha='center', fontsize=12)

ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1)

plt.show()
