import pandas as pd

def clean_employee_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Settle the messy employee dataset nicely using a steady 5-step workflow, don't play play.
    """
    print(f"--- Step 1 & 2: Steady bom piak, load dataset & settle Encoding/Delimiter hor ---")
    try:
        df = pd.read_csv(input_path, encoding='utf-8', on_bad_lines='skip')
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding='latin1', on_bad_lines='skip')
    
    print("\n[Wah, see the initial info first]:")
    print(df.info())
    print("\n[A bit of sample data to kaypoh]:")
    print(df.head())

    print("\n--- Step 3: Chop carrot head, fix Data Types properly ---")
    if 'employee_id' in df.columns:
        df['employee_id'] = df['employee_id'].astype(str)
    if 'salary' in df.columns:
        df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

    print("\n--- Step 4: Arrow the date columns, use pd.to_datetime() faster ---")
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'join' in col.lower() or 'dob' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    print("\n--- Step 5: Chop-chop blur blur standardise Categorical Columns (strip space, make nice capital) ---")
    categorical_cols = df.select_dtypes(include=['object', 'string']).columns
    for col in categorical_cols:
        df[col] = df[col].astype(str).str.strip().str.title()
        df[col] = df[col].replace({'Nan': None, 'None': None, '': None})

    print("\n--- Final check liao (Final Audit) & Save file ---")
    print("\n[See got how many missing values or not]:")
    print(df.isnull().sum())
    
    print("\n[Shiok! Dataset info after clearing up]:")
    print(df.info())

    # Export out nicely, don't chao-sng
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\n[Settle nicely] Saved clean file already: {output_path}. Mai tu liao, go upload to GitHub liao hor!")
    return df

if __name__ == "__main__":
    INPUT_FILE = "data/raw_employees.csv"
    OUTPUT_FILE = "data/cleaned_employees.csv"
    
    clean_employee_data(INPUT_FILE, OUTPUT_FILE)
