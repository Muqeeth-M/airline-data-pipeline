import pandas as pd
import os 

# --- load all 3 csv files --------------
base_path = os.path.join(os.path.dirname(__file__), '..', 'data')

df1 = pd.read_csv(os.path.join(base_path, 'Airline Dataset.csv'))
df2 = pd.read_csv(os.path.join(base_path, 'Airline Dataset updated.csv'))
df3 = pd.read_csv(os.path.join(base_path, 'Airline Dataset Updated - v2.csv'))

print(f"File 1 rows: {len(df1)}")
print(f"File 2 rows: {len(df2)}")
print(f"File 3 rows: {len(df3)}")

# ------combine all 3 files into one -----------
df = pd.concat([df1,df2,df3],ignore_index = True)
print(f"\nTotal rows after combining: {len(df)}")

# ---- remove columns (remove spaces) ----------
df.columns = [col.strip().replace(' ', '_') for col in df.columns]

# --- drop duplicates rows --------------
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
print(f"Duplicates removed: {before - after}")

# ----drop rows where critical fields are null -------------
df.dropna(subset=['Passenger_ID', 'Departure_Date', 'Flight_Status'], inplace=True)

# ------ clean text columns -----------------------
text_cols = ['First_Name', 'Last_Name', 'Gender', 'Nationality', 'Airport_Name', 'Country_Name', 'Pilot_Name', 'Flight_Status']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()

# ------fix date formats -----------------------
df['Departure_Date'] = pd.to_datetime(df['Departure_Date'], errors='coerce')
df.dropna(subset=['Departure_Date'], inplace = True)
df['Departure_Date'] = df['Departure_Date'].dt.strftime('%Y-%m-%d')

# ------ Standardize flight status values ------------------
df['Flight_Status'] = df['Flight_Status'].str.strip().str.title()
print(f"\nFlight Status values : {df['Flight_Status'].unique()}")

# ---- Age Validation ------------------------
df = df[df['Age'].between(1, 100, inclusive = 'both')]

# ---- Final Summary --------------------------------
print(f"\nFinal clean rows : {len(df)}")
print(f"Columns : {list(df.columns)}")

# ---- save cleanned file -----------------
output_path = os.path.join(base_path, 'Cleaned_Airline_Data.csv')
df.to_csv(output_path, index=False)
print(f"\n Cleaned data saved to: {output_path}")


