import pandas as pd
df1 = pd.read_csv('sales_sep_200.csv')
df2 = pd.read_csv('customers_100.csv')
df3 = pd.read_csv('products_030.csv')
print(df4= df1['product_id'].value_counts().sort_values(ascending=False))
print()