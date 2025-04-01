import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/simple-Linear-Regression/master/Salary_Data.csv')
print(df.head())
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='YearsExperience',y='Salary',data=df)
plt.show()
# Fit a line
# Plot 1
import numpy as np
b=25792
w=8449
x=np.linspace(0,12,100)
y=w*x+b
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.scatterplot(x='YearsExperience',y='Salary',data=df)
plt.plot(x,y,c='red')
plt.title('b=25792,w=8449')
# Plot 2
b=35892
w=8349
x=np.linspace(0,12,100)
y=b+w*x
plt.subplot(1,2,2)
sns.scatterplot(x='YearsExperience',y='Salary',data=df)
plt.plot(x,y,c='yellow')
plt.title('b=35892,w=8349')
plt.tight_layout()
plt.show()