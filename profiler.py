import pandas as pd
import sys

def profile_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        print("\n===== CSV DATA PROFILER =====\n")
        print(f"File: {file_path}")
        print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

        print("----- Column Info -----")
        print(df.info())

        print("\n----- Missing Values -----")
        print(df.isnull().sum())

        print("\n----- Summary Statistics -----")
        print(df.describe(include='all'))

        print("\n----- Correlation Matrix -----")
        print(df.corr(numeric_only=True))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python profiler.py <file.csv>")
    else:
        profile_csv(sys.argv[1])
