print("Sales Data Analyst Project Started")
import pandas as pd

# Excel file ka path
file_path = "raw_data1/Sales_Data_Mock.xlsx"

# Excel data Python mein load karna
df = pd.read_excel(file_path)

print(df)
print("\nShape of data:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Row:")
print(df.duplicated().sum())
print("\nUnique Region Values:")
print(df["Region"].unique())
print("\nUnique Category Values:")
print(df["Category"].unique())
print("\nData Types:")
print(df.dtypes)
print("\nStatisticak Summary:")
print(df.describe())
print("\nMinimum Values:")
print(df[["Quantity", "UnitPrice", "SalesAmount"]].min())

print("\nMaximum Values:")
print(df[["Quantity", "UnitPrice", "SalesAmount"]].max())
print("\nDiscount Range:")
print("Minimum Discount:", df["Discount(%)"].min())
print("Maximum Discount:", df["Discount(%)"].max())
print("\nCleaning Region Values...")

df["Region"] = df["Region"].str.strip().str.title()

print(df["Region"].unique())
# Cleaned data ko Excel file mein save karna
output_path = "raw_data1/Sales_Data_Cleaned.xlsx"

df.to_excel(output_path, index=False)

print("\nCleaned data saved successfully!")
print("File:", output_path)
# Cleaned file ko dobara load karke verify karna
cleaned_df = pd.read_excel(output_path, engine="openpyxl")

print("\nCleaned Data Shape:")
print(cleaned_df.shape)

print("\nCleaned Region Values:")
print(cleaned_df["Region"].unique())
print("\nMissing Values After Cleaning:")
print(cleaned_df.isnull().sum())
print("\nDuplicate Rows After Cleaning:")
print(cleaned_df.duplicated().sum())
print("\nInvalid Unit Price Values:")
print((cleaned_df["UnitPrice"] <=0).sum())
print("\nInvalid Discount Values:")
print(((cleaned_df["Discount(%)"] < 0) | (cleaned_df["Discount(%)"] > 100)).sum())
print("\nFinal Cleaned Data Preview:")
print(cleaned_df.head())

