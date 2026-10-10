import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())
