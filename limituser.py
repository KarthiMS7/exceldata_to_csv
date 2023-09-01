import pandas as pd

def filter_and_generate_csv(input_excel_path, output_csv_path):
    # Step 1: Read the Excel file, skipping rows with all NaN values
    excel_data = pd.read_excel(input_excel_path)
    # Remove rows with all NaN values
    excel_data = excel_data.dropna(how='all')
    
    # Remove extra spaces from column names
    excel_data.columns = excel_data.columns.str.strip()
    
    print(excel_data.columns)

    # Specify the required columns
    required_columns = ['Name', 'User ID', 'Machine Name', 'Expiry Date for access', 'Email ID', 'Phone Number']

    # Filter the DataFrame to select only the required columns
    filtered_data = excel_data[required_columns]

    # Step 2: Generate CSV with required fields
    filtered_data.to_csv(output_csv_path, index=False)
    print(f'Saved {output_csv_path}')

if __name__ == "__main__":
    # Specify the input Excel file path and output CSV file path
    input_excel_path = r'sample_user_tracking_file.xlsx'
    output_csv_path = r'output.csv'  
    filter_and_generate_csv(input_excel_path, output_csv_path)
