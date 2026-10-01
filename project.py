import pandas as pd

# ============================================================
# 1. LOAD CSV FILE AND DISPLAY BASIC INFORMATION
# ============================================================

# Load CSV file
df = pd.read_csv("cleaned_sales_data.csv")

print("=" * 60)
print("1. BASIC INFORMATION")
print("=" * 60)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display information about dataset
print("\nDataset Information:")
df.info()


# ============================================================
# 2. HANDLE MISSING VALUES AND DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("2. MISSING VALUES AND DUPLICATES")
print("=" * 60)

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Convert value column into numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Fill missing values in value column with 0
df["value"] = df["value"].fillna(0)

# Count duplicates
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# 3. GROUP DATA BY CATEGORY AND FIND TOTAL VALUE
# ============================================================

print("\n" + "=" * 60)
print("3. TOTAL VALUE BY CATEGORY")
print("=" * 60)

# Group data by industry
total_value = df.groupby(
    "industry_name_ANZSIC"
)["value"].sum()

print("\nTotal Value for Each Industry:")
print(total_value)


# ============================================================
# 4. SORT DATA BY MULTIPLE COLUMNS
# ============================================================

print("\n" + "=" * 60)
print("4. SORT DATA BY MULTIPLE COLUMNS")
print("=" * 60)

# Sort by industry name (A-Z)
# and year (highest to lowest)
sorted_data = df.sort_values(
    by=["industry_name_ANZSIC", "year"],
    ascending=[True, False]
)

print("\nSorted Data:")
print(sorted_data.head(20))


# ============================================================
# 5. CREATE CORRELATION MATRIX
# ============================================================

print("\n" + "=" * 60)
print("5. CORRELATION MATRIX")
print("=" * 60)

# Select numerical columns
numeric_data = df.select_dtypes(include="number")

# Create correlation matrix
correlation_matrix = numeric_data.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)


# ============================================================
# SAVE RESULTS
# ============================================================

# Save cleaned data
df.to_csv("cleaned_output.csv", index=False)

# Save total value by industry
total_value.to_csv("total_value_by_industry.csv")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nFiles created:")
print("1. cleaned_output.csv")
print("2. total_value_by_industry.csv")