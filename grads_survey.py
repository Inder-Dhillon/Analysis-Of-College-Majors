import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
recent_grads = pd.read_csv('recent-grads.csv')
#Inspecting value count
#print(recent_grads.describe())

#Dropping rows with missing values so matplotlib doesn't act up
recent_grads = recent_grads.dropna(axis=0)
print(recent_grads.describe())
fig, axes = plt.subplots(nrows=2, ncols=3)
recent_grads.plot(x="Sample_size", y="Median", kind="scatter", ax=axes[0,0], figsize=(15,7))
recent_grads.plot(x="Sample_size", y="Unemployment_rate", kind="scatter", ax=axes[0,1])
recent_grads.plot(x="Full_time", y="Median", kind="scatter", ax=axes[0,2])
recent_grads.plot(x="ShareWomen", y="Unemployment_rate", kind="scatter", ax=axes[1,0])
recent_grads.plot(x="Men",  y="Median", kind="scatter", ax=axes[1,1])
recent_grads.plot(x="Women",  y="Median", kind="scatter", ax=axes[1,2])
plt.show()

