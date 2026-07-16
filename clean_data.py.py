import pandas as pd

# 1. Load the original raw dataset
# Ensure the Excel file is in the same folder as this script
df = pd.read_excel('Copy of Dataset for Data Analytics.xlsx')

# 2. Fill missing CouponCode with 'NONE'
df['CouponCode'] = df['CouponCode'].fillna('NONE')

# 3. Ensure date format is YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# 4. Ensure numeric precision (2 decimals)
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)

# 5. Save the cleaned version to a new file
# This creates a brand new, clean spreadsheet
df.to_excel('Cleaned_Dataset_for_Data_Analytics.xlsx', index=False)

print("Cleaning complete. Cleaned_Dataset_for_Data_Analytics.xlsx has been created.")