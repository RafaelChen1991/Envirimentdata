from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import datetime as dt



df1 = pd.read_excel('2018-03-30~ 2019-05-31.xlsx')
df2 = pd.read_excel('2017-04-09~2018-03-30.xlsx')
df = pd.concat([df1, df2])
# df = pd.read_excel('20190425_2.xlsx')

df['week'] = df['時間日期'].dt.weekofyear


df['time'] = df['時間日期'].dt.strftime('%H:%M:%S')
df['month'] = df['時間日期'].dt.strftime('%m')
df['year'] = df['時間日期'].dt.strftime('%Y')

df['month'] = pd.DataFrame(df['month'], dtype=np.int)
df['year'] = pd.DataFrame(df['year'], dtype=np.int)
#df['time'] = pd.to_datetime(df['time'], format = '%H:%M:%S')



def dayornight(light):
	if light > 100:
		return "day"
	else:
		return "night"


df['dorn'] = df.apply(lambda x: dayornight(x.屋外光度), axis = 1)



# avgtem = df["屋外溫度"].groupby([df['year'], df['month'], df['dorn']]).mean()
# #print(avgtem)
# avgtem.unstack().plot()

# avgtemA = df["zoneA棟溫度"].groupby([df['year'], df['month'], df['dorn']]).mean()
# #print(avgtemA)
# avgtemA.unstack().plot()

# avgtemB = df["zoneB棟溫度"].groupby([df['year'], df['month'], df['dorn']]).mean()
# #print(avgtemB)
# avgtemB.unstack().plot()

# plt.show()


sumli = df["屋外光度"].groupby([df['year'], df['week'], df['dorn']]).sum()
print(sumli)
sumli.to_excel("sumli.xlsx")
# sumli.unstack().plot()

sumliA = df["zoneA棟光度"].groupby([df['year'], df['week'], df['dorn']]).sum()
print(sumliA)
sumliA.to_excel("sumliA.xlsx")
# sumliA = sumliA.unstack().plot()

sumliB = df["zoneB棟光度"].groupby([df['year'], df['week'], df['dorn']]).sum()
print(sumliB)
sumliB.to_excel("sumliB.xlsx")
# sumliB = sumliB.unstack().plot()

# plt.show()



# avghum = df["屋外濕度"].groupby([df['year'], df['month'], df['dorn']]).mean()
#print(avghum)
# avghum.unstack().plot()

# avghumA = df["zoneA棟濕度"].groupby([df['year'], df['month'], df['dorn']]).mean()
#print(avghumA)
# avghumA.unstack().plot()

# avghumB = df["zoneB棟濕度"].groupby([df['year'], df['month'], df['dorn']]).mean()
#print(avghumB)
# avghumB.unstack().plot()

# plt.show()



#print(df.describe())

# df.shape
#df.columns
#df.index
#df.info()
#df.describe()

#for row in df.itertuples()


#sumliA.to_excel("sumliA.xlsx")




#df.plot.scatter(x='屋外光度', y='屋外濕度',c='屋外溫度')
#plt.show()

