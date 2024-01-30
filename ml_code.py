import pandas as pd
import numpy as np

df = pd.read_csv('FINAL.csv')
df.drop(['Unnamed: 0'], axis = 1, inplace= True)

#duplicate removal
#print(df.shape)
#print(df.duplicated().sum())
df1 = df.copy()
#print(df1.shape)
df1.drop_duplicates(inplace=True)
#print(df1.shape)

#na removal
#print(df1.isna().sum())
df1.drop(['Availability'], axis = 1, inplace = True)
#print(df1.shape)



types = list(df['Type'].unique())
print(types)
print(df['Type'].value_counts())

for
cnt = 0
for i in range(len(df1)):
    if pd.isna(df1.iloc[i, 0]) and pd.isna(df1.iloc[i,1]):
        df1.iloc[i, 0] = df1.iloc[i,-2]
        #df1.iloc[i, 1] = [x for x in]
        print(df1.iloc[i,:])
        cnt += 1
print(cnt)
