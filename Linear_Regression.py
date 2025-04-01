import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/kvinlazy/Dataset/master/FuelConsumptionCo2.csv')
print(df.head())
df=df[['ENGINESIZE','CYLINDERS','CO2EMISSIONS']]
print(df.describe())
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='CYLINDERS',y='ENGINESIZE',hue='CO2EMISSIONS',data=df)
plt.show()
fig,axes=plt.subplots(1,2,figsize=(12,5))
sns.scatterplot(x='ENGINESIZE',y='CO2EMISSIONS',data=df,ax=axes[0])
axes[0].set_title('Engine Size vs CO2 Emissions')
sns.scatterplot(x='CYLINDERS',y='CO2EMISSIONS',data=df,ax=axes[1])
axes[1].set_title('Cylinders vs CO2 Emissions')
plt.tight_layout()
plt.show()