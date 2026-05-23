import pandas as pd

sales = pd.read_csv('data/sales.csv')
customers = pd.read_csv('data/customers.csv')
products = pd.read_csv('data/products.csv')

df = sales.merge(customers,on='customer_id')
df = df.merge(products,on='product_id')

df['revenue'] = df['qty'] * df['price']

df.to_csv('data/final_sales.csv',index=False)