# -------------------------------
# 🧠 STEP 1: IMPORT LIBRARIES
# -------------------------------

# pandas is the main library used for data handling (reading CSV, filtering, etc.)
import pandas as pd


# -------------------------------
# 🧾 STEP 2: LOAD YOUR CSV FILE
# -------------------------------

# Read the CSV file and store it in a variable called df (which stands for "DataFrame")
# r'' means raw string — it tells Python not to treat \ as special characters
# Make sure the file path below matches where you saved your students.csv
df = pd.read_csv(r'C:\Python test data\students.csv')


# -------------------------------
# 👀 STEP 3: VIEW THE FIRST FEW ROWS
# -------------------------------

# .head() shows the top 5 rows of the file — helps confirm the file loaded correctly
print("🔹 First few rows of your data:")
print(df.head())   # prints the first 5 rows
print()            # blank line for readability


# -------------------------------
# 📏 STEP 4: CHECK DATA SHAPE (ROWS & COLUMNS)
# -------------------------------

# .shape returns a tuple (number_of_rows, number_of_columns)
print("🔹 Shape of your data (rows, columns):", df.shape)
print("Rows:", df.shape[0])     # total number of rows
print("Columns:", df.shape[1])  # total number of columns
print()


# -------------------------------
# 🧱 STEP 5: SEE COLUMN INFO
# -------------------------------

# .info() shows:
# - Each column name
# - How many values are NOT missing
# - What data type each column contains (int, float, or object = text)
print("🔹 Data information and types:")
print(df.info())
print()


# -------------------------------
# 🚨 STEP 6: CHECK FOR MISSING DATA
# -------------------------------

# .isnull().sum() counts how many empty (NaN) values are in each column
print("🔹 Missing values in each column:")
print(df.isnull().sum())
print()


# -------------------------------
# 📊 STEP 7: QUICK STATISTICS SUMMARY
# -------------------------------

# .describe() gives basic stats for numeric columns — like mean, min, max, etc.
print("🔹 Basic statistics for numeric columns:")
print(df.describe())
print()


# -------------------------------
# 🧩 STEP 8: VIEW UNIQUE VALUES IN A COLUMN
# -------------------------------

# .unique() shows all unique entries in a column — here we check 'subject'
print("🔹 Unique subjects found in the file:")
print(df['subject'].unique())
print()


# -------------------------------
# ✅ BONUS: OPTIONAL — CHECK COLUMN NAMES
# -------------------------------

# .columns shows a list of all column names — useful if you forget or need to rename them
print("🔹 Column names:")
print(df.columns)
print()


# -------------------------------
# 🎉 DONE!
# -------------------------------

print("✅ Data successfully loaded and inspected!")
