# Use with %load imports.py
%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.interactiveshell import InteractiveShell

%config InlineBackend.figure_format = "retina" # Higher resolution plots

InteractiveShell.ast_node_interactivity = "all" # Muliple outputs
plt.style.use('C:\\Users\\pcosta\\DSwork\\referece_files\\material.mplstyle') # My Matplotlib style

# Plot references
# plt.axhline(0, c='#9E9E9E', zorder=1) Origin line
# plt.title('Lorep ipsum', loc='left') Title
# plt.legend(bbox_to_anchor=(1,1), loc='upper left') Legend
# plt.scatter(x, y, alpha=0.5, label='Lorep', s=100, linewidths=0, zorder=2) Scatter
