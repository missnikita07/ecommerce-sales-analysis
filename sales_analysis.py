import pandas as pd

# Load Dataset
df = pd.read_csv("Dataset/SampleSuperstore.csv")

print("===== DATASET INFORMATION =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== TOTAL SALES =====")
print(round(df['Sales'].sum(),2))

print("\n===== TOTAL PROFIT =====")
print(round(df['Profit'].sum(),2))

print("\n===== SALES BY CATEGORY =====")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

print("\n===== PROFIT BY CATEGORY =====")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

print("\n===== SALES BY REGION =====")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print("\n===== TOP 10 STATES BY SALES =====")
print(df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10))
import matplotlib.pyplot as plt

# Sales by Category Chart
sales_category = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))
sales_category.plot(kind='bar')
plt.title('Sales by Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('Python/sales_by_category.png')
plt.show()


# Sales by Region

sales_region = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))
sales_region.plot(kind='bar')
plt.title('Sales by Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('Python/sales_by_region.png')
plt.show()


# Profit by Category

profit_category = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind='bar')
plt.title('Profit by Category')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('Python/profit_by_category.png')
plt.show()