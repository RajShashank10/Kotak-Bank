import pandas as pd
df = r"C:\Users\Vikas\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv"
try:
    df = pd.read_csv(df)
    print("File read successfully!")
    print("Total Rows:", len(df))
    print("Total Columns:", len(df.columns))
    print("\nColumn Names:")
    print(df.columns)
    print("\nFirst 10 Rows:")
    print(df.head(10))
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("Error Type:", e)