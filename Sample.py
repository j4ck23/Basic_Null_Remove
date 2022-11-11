import pandas as pd

df = pd.read_csv("out_csv.csv")#Reads csv to a pandas dataframe

df = df.sample(n = 10000)#Randomly selcet 10000 rows

df.to_csv("Sampled2.csv", encoding='utf-8')#Outputs formated data