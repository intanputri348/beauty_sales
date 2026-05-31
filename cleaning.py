import pandas as pd
import numpy as np

products = pd.read_csv("product_code.csv")
transactions = pd.read_csv("transactions.csv")

print(products.head())
print(products.info())

print(transactions.head())
print(transactions.info())

# Cek baris dan kolom 
print(products.shape)
print(transactions.shape)

# Cek duplicates pada product_code
print(products.duplicated(subset='product_code').sum())

# Cek duplicates pada transaction
print(transactions.duplicated(subset='transaction_id').sum())

# Cek Missing Values
print(products.isnull().sum())
print(transactions.isnull().sum())

# Cek missing return_reason terjadi di transaksi return atau non-return?
print(
    transactions.groupby('returned_flag')['return_reason']
    .apply(lambda x: x.isnull().sum())
)

transactions.loc[
    (transactions['returned_flag'] == 'No') &
    (transactions['return_reason'].isnull()),
    'return_reason'
] = 'No Return'

transactions.loc[
    (transactions['returned_flag'] == 'Yes') &
    (transactions['return_reason'].isnull()),
    'return_reason'
] = 'Unknown Return Reason'

print(transactions['return_reason'].isnull().sum())

# Convert transaction_date
transactions['transaction_date'] = pd.to_datetime(
    transactions['transaction_date'], 
    format='%d/%m/%Y'
)
# Memastikan numerik
numeric_cols = [
    'quantity',
    'gross_sales',
    'discount_amount',
    'net_sales',
    'platform_fee',
    'customer_rating'
]

for col in numeric_cols:
    transactions[col] = pd.to_numeric(
        transactions[col],
        errors='coerce'
    )

# Cek Nilai Negatif
transactions = transactions[transactions['quantity'] > 0]
transactions = transactions[transactions['net_sales'] >= 0]
transactions = transactions[transactions['net_sales'] >= 0]

# Validasi Net Sales
transactions['calculated_net_sales'] = (
    transactions['gross_sales']
    - transactions['discount_amount']
)

invalid_sales = transactions[
    transactions['calculated_net_sales']
    != transactions['net_sales']
]

print(invalid_sales)

# Standarisasi Teks
transactions['platform'] = (
    transactions['platform']
    .str.strip()
    .str.title()
)

# Bersihkan Returned Flag
transactions['returned_flag'] = (
    transactions['returned_flag']
    .str.strip()
    .str.title()
)

# Merge Dataset
final_df = transactions.merge(
    products,
    on='product_code',
    how='left'
)

# Cek Product yang Tidak Match
print(final_df['product_name'].isnull().sum())

# Membuat kolom Profit
final_df['profit'] = (
    final_df['net_sales']
    - final_df['platform_fee']
    - (final_df['production_cost']
       * final_df['quantity'])
)

# Membuat Profit Margin
final_df['profit_margin'] = (
    final_df['profit']
    / final_df['net_sales']
)

# Tambahkan Kolom Tanggal
final_df['year'] = (
    final_df['transaction_date'].dt.year
)
final_df['month'] = (
    final_df['transaction_date'].dt.month_name()
)
final_df['quarter'] = (
    'Q' +
    final_df['transaction_date']
    .dt.quarter.astype(str)
)

print(final_df['net_sales'].describe())

# Cek Null Setelah Merge
print(final_df.isnull().sum())

# Menyimpan Dataset
final_df.to_csv(
    'cleaned_beauty_sales.csv',
    index=False
)