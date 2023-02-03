import matplotlib.pyplot as plt 
import matplotlib.ticker as tkr
import seaborn as sns
sns.set(font_scale=1.4)

labels = df['channel'].value_counts().index.to_list()
values = df['channel'].value_counts().to_list()
width = 0.35

fig, ax = plt.subplots(figsize=(14, 10))
ax.yaxis.set_major_formatter(
        tkr.FuncFormatter(lambda y,  p: format(int(y), ',')))
bars = ax.bar(labels, values, width, color='b')
container = ax.containers[0]
ax.bar_label(bars, labels=[f'{x:,.0f}' for x in container.datavalues], size=14)
plt.xlabel("Channel", labelpad=14)
plt.ylabel("Count of Unique Members", labelpad=14)
plt.title("PCP HPSA Members with Email by Channel", y=1.02);