import pandas as pd 
import numpy as np 
import datetime
import random

products = {
    'iPhone': [700,10],
    'Google Phone': [680,8],
    'Vareebadd Phone':[400,2],
    '20in Monitor':[109.99,3],
    '34in Ultrawide Monitor':[379.99,5],
    '27in $K Gaming Monitor':[389.99,5],
    '27in FHD Monitor':[149.99,4],
    'Flatscreen TV':[300,5],
    'Macbook Pro Laptop':[1700,4],
    'ThinkPad Laptop':[999.99,8],
    'AA Batteries':[3.84,4],
    '34ins Ultrawide Monitor':[890.99,2],
    '27ins $K Gaming Monitor':[388.99,5],
    '27ins FHD Monitor':[149.99,5],
    'Flatscreens TV':[300,4],
    'Macbooks Pro Laptop':[1700,9],
    'ThinkPads Laptop':[999.99,6],
    'AA Batterie':[3.84,4],

}
columns = ['Order ID','Product','Quantity Order','Price','Ordered Date','Purchase Address']

df = pd.DataFrame(columns=columns)
print(df)
for i in range(1000):
    product_list = [product for product in products]
    weights = [products[product][1] for product in products]
    product = random.choices(product_list,weights=weights)[0]
    price = products[product]
    df.loc[i] = [i,product,1,price,"NA","NA"]
print(product_list)
print(weights)
df.to_csv("test_data.csv")