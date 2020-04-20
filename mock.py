import pandas as pd 
import numpy as np 
import datetime
import random
import calendar

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
def write_row(order_id,product,order_date,address):
    price = products[product][0]
    quantity_ordered = np.random.geometric(p=1.0-(1.0/price),size=1)[0]
    return [order_id,product,quantity_ordered,price,date,address]
def generate_random_time(month):
    # format mm/dd/yr H:m
    dayrange = calendar.monthrange(2019,month)[1]
    random_day = random.randint(1,dayrange)
    if random.random() < 0.5:
        date = datetime.datetime(2020,month,random_day,12,0)
    else:
        date = datetime.datetime(2020,month,random_day,20,0)
    time_offset = np.random.normal(loc=0,scale=180)
    final_date = date + datetime.timedelta(minutes=time_offset)
    # pass
    return final_date.strftime("%m/%d/%y %H:%M")
def generate_random_address():
    street_names = ['Main','2nd','3rd','4th','5th','Park','Maple','Pine','Washington','8th']
    cities = ['Nairobi','Kericho','Nakuru','Kisii','Nairobi','Mombasa','Portland','Portland','Kajiado','kitengela']
    states = ['A','B','C','D','E','F','G','H','I','J']
    weights = [9,4,9,3,5,10,2,9,4,9]
    zips = ['55','66','88','99','101','102','103','104','128','129']
    street = random.choice(street_names)
    index = random.choices(range(len(cities)),weights=weights)[0]
    return f"{random.randint(1,999)} { street} St,{cities[index]},{states[index]} {zips[index]}"

if __name__ == "__main__":
    product_list = [product for product in products]
    weights = [products[product][1] for product in products]
    columns = ['Order ID','Product','Quantity Order','Price','Ordered Date','Purchase Address']
    # print(df)
    order_id = 143253
    for month_value in range(1,13):
        if month_value <= 10:
            # orders_amount = 100
            orders_amount = int(np.random.normal(loc=12000,scale=4000))
            print(orders_amount)
            pass
        if month_value == 11:
            # orders_amount = 150
            orders_amount = int(np.random.normal(loc=20000,scale=3000))
            print(orders_amount)
            pass
        if month_value == 12:
            # orders_amount = 200
            orders_amount = int(np.random.normal(loc=26000,scale=4000))
            print(orders_amount)
            pass
        df = pd.DataFrame(columns=columns)
        # for i in range(orders_amount):
        i = 0
        while orders_amount > 0:
            address = generate_random_address()
            date = generate_random_time(month_value)
            # print(date)
            product = random.choices(product_list,weights=weights)[0]
            # print(quantity_ordered)
            df.loc[i] = write_row(order_id,product,date,address)
            if product == "iPhone":
                if random.random() < 0.15:
                    df.loc[i] = write_row(order_id,"Macbook Pro Laptop",date,address)
                    i += 1
                # else:
            i += 1
            order_id += 1
            orders_amount -= 1
        month_name = calendar.month_name[month_value]
        print(month_name)
        df.to_csv(f"{month_name}_test_data.csv")
        print("done")