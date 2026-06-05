# MOBILE PHONE DATA ANALYSIS PROJECT 

import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

df = pd.read_csv("Mobile.csv")

print("\nDATA PREVIEW")
print(df.head())

# DATA CLEANING

# Clean Battery 
df['Battery_power_mAh'] = df['Battery_power_mAh'].str.replace(' mAh','')
df['Battery_power_mAh'] = df['Battery_power_mAh'].astype(int)

# Clean RAM 
df['Ram_mb'] = df['Ram_mb'].str.extract('(\d+)').astype(int)

# Convert Yes/No to 1/0
binary_cols = ['Bluetooh', 'Dual_sim', '3G', 'touch_screen', 'wifi']

for col in binary_cols:
    df[col] = df[col].map({'Yes':1, 'No':0})

# Convert price_range to numeric
mapping = {
    "Low cost": 0,
    "Medium cost": 1,
    "High cost": 2,
    "Very high cost": 3
}
df['price_range'] = df['price_range'].map(mapping)

# Remove missing values
df = df.dropna()

print("\nCLEANED DATA INFO")
print(df.info())

# BASIC ANALYSIS

print("\nBASIC STATISTICS")
print(df.describe())

# CORRELATION 

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

print("\nFEATURE IMPACT ON PRICE")
print(correlation['price_range'].sort_values(ascending=False))

# VISUALIZATION

# RAM vs Price
plt.scatter(df['Ram_mb'], df['price_range'])
plt.xlabel("RAM (MB)")
plt.ylabel("Price Range")
plt.title("RAM vs Price Category")
plt.show()

# Battery vs Price
plt.scatter(df['Battery_power_mAh'], df['price_range'])
plt.xlabel("Battery Power (mAh)")
plt.ylabel("Price Range")
plt.title("Battery vs Price Category")
plt.show()

# CATEGORY ANALYSIS

grouped = numeric_df.groupby(df['price_range']).mean()

print("\nAVERAGE FEATURES BY PRICE CATEGORY")
print(grouped[['Ram_mb', 'Battery_power_mAh']])

grouped[['Ram_mb','Battery_power_mAh']].plot(kind='bar')
plt.title("Feature Comparison by Price Category")
plt.show()

# FINAL INSIGHTS

print("\nFINAL INSIGHTS")

# Most important feature
most_important = correlation['price_range'].drop('price_range').idxmax()
print(f"Most important feature affecting price: {most_important}")

print("Phones with higher RAM generally belong to higher price categories.")
print("Battery power has moderate influence on price.")
print("Price depends on a combination of multiple features.")