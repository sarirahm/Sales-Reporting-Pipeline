from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://user:password@localhost/sales_dw"
)

df = pd.read_csv('data/final_sales.csv')

df.to_sql(
    'sales_mart',
    engine,
    if_exists='replace',
    index=False
)