import pandas as pd
import csv

db = pd.read_csv(r"E:\PythonProjects\WorkWithCSV\BlackFriday.csv")
cnt = db.groupby(['User_ID']).size().reset_index()
print(db)

z1 = db.Age.unique()
print("Возрастных категорий участвовало в акции? : ",len(z1))

z2 = len(db[(db['Gender'] == 'M') & (db['City_Category'] == 'A')])
print("Мужчин из города категории A : ",z2)

z3 = len(db[(db['Age'] == '46-50') & (db['Gender'] == 'F') & (db['Purchase'] > 20000)])
print("Женщин от 46 до 50, потративших больше 20000 : ",z3)

z4 = db.Product_Category_3.isna().sum()
print("NaN'ов в столбце Product_Category_3 : ",z4)

z5 = len(db[(db['Gender'] == 'M') & (db['Age']=='26-35') | (db['Gender'] == 'F') & ((db['Age']=='36-45') | (db['Age']=='46-50') | (db['Age']=='51-55') | (db['Age']=='55+'))])
print("Какую долю от всех покупателей составляют ВМЕСТЕ мужчины от 26 до 35 лет и женщины старше 36 лет? :",z5)
