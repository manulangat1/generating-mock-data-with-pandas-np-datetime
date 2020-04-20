import pandas as pd 
import numpy as np 
import datetime
import random

products = {
    'iPhone': 700,
    'Google Phone': 680,
    'Vareebadd Phone':400,
    '20in Monitor':109.99,
    '34in Ultrawide Monitor':379.99,
    '27in $K Gaming Monitor':389.99,
    '27in FHD Monitor':149.99,
    'Flatscreen TV':300,
    'Macbook Pro Laptop':1700,
    'ThinkPad Laptop':999.99,
    'AA Batteries':3.84,
    '34ins Ultrawide Monitor':890.99,
    '27ins $K Gaming Monitor':388.99,
    '27ins FHD Monitor':149.99,
    'Flatscreens TV':300,
    'Macbooks Pro Laptop':1700,
    'ThinkPads Laptop':999.99,
    'AA Batterie':3.84,

}
columns = ['Order ID','Product','Quantity Order','Price','Ordered Date','Purchase Address']

df = pd.DataFrame(columns=columns)
print(df)
for i in range(1000):