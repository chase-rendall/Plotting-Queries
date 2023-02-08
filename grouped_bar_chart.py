# Group bar chart plot
import matplotlib.pyplot as plt
import numpy as np

N = 5
values1 = [10, 14, 7, 35, 21]
values2 = [8, 29, 15, 64, 23]

ind = np.arange(N)    # X locations for the groups
width = 0.35          # width of bars

fig, ax = plt.subplots(figsize=(8,6))
rects1 = ax.bar(ind, values1, width, color='royalblue', label='Men')
rects2 = ax.bar(ind, values2, width, color='seagreen', label='Women')

for bars in ax.containers:
    ax.bar_label(bars)

ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend();
