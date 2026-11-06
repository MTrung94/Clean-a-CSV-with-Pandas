https://roadmap.sh/projects/clean-csv

# Clean a CSV with Pandas

A Python data cleaning tool designed to process and normalize a messy synthetic employee dataset into a clean, structured format.

## Features & Cleaning Steps
1. **Encoding & Delimiter Handling:** Safely loads CSV datasets with potential encoding issues or bad lines.
2. **Data Type Enforcement:** Fixes column data types explicitly (`dtype` / `to_numeric`).
3. **Date Standardization:** Converts date attributes using `pd.to_datetime()` with `errors='coerce'`.
4. **Categorical Normalization:** Strips trailing whitespaces and unifies letter casing across text fields.
5. **Final Audit & Export:** Generates missing-value summaries and exports clean data to `data/cleaned_employees.csv`.

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
