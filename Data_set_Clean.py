import pandas as pd

df = pd.read_csv("police_project.csv")#Reads csv to a pandas dataframe
df = df.drop('county_name',axis=1)#Drops the country name column
df = df.drop('search_type',axis=1)#Drops the serach type column

df.dropna(inplace = True)#Drops any row with a null value

for c_test in df:
    print(df[c_test].isnull().sum())#Loops through each column and sums any null value
    #If output not 0 null vlaues still remain

df.to_csv("out_csv.csv", sep='\t', encoding='utf-8')#Outputs formated data