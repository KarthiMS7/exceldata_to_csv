# exceldata_to_csv


# Excel to CSV Converter

## Introduction

This Python script allows you to convert Excel files into CSV format. It's particularly useful when you have Excel data that you want to work with in other applications or tools that support CSV.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python (version 3.x)
- pandas library (can be installed via pip)

```bash
pip install pandas
```

## Usage

1. Clone or download this repository to your local machine.

2. Place the Excel files you want to convert into the same directory as `limituser.py`.

3. Open a terminal or command prompt and navigate to the directory containing `limituser.py`.

4. Run the script using the following command:

```bash
python limituser.py
```

5. The script will read Excel files in the current directory, process them, and generate corresponding CSV files.

## Configuration

You can customize the script by modifying the `required_columns` variable in the script to specify the columns you want to include in the CSV output.

```python
required_columns = ['Name', 'User ID', 'Machine Name', 'Expiry Date for access', 'Email ID', 'Phone Number']
```

## Example

Here's an example of how to use the script:

Suppose you have an Excel file named `data.xlsx` with the following columns: Name, User ID, Machine Name, Expiry Date for access, Email ID, Phone Number.

1. Place `data.xlsx` in the same directory as `limituser.py`.

2. Run the script as mentioned in the "Usage" section.

3. The script will generate a CSV file named `data.csv` containing the specified columns from the Excel file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pandas](https://pandas.pydata.org/) library for data manipulation.
- [GitHub](https://github.com/) for version control and collaboration.

Feel free to customize this README file further to include any additional information, project details, or acknowledgments specific to your use case.
