import csv

# Input CSV file name
input_file = 'C:/Users/joeas/Downloads/1543384-70_Écritures_03-05-2024.csv'

# Output CSV file name (without the first 5 rows)
output_file = 'C:/Users/joeas/Downloads/output.csv'

# Function to skip first n rows in a CSV file
def skip_rows(input_file, output_file, n):
    with open(input_file, 'r', newline='') as f_input:
        with open(output_file, 'w', newline='') as f_output:
            reader = csv.reader(f_input)
            writer = csv.writer(f_output)

            # Skip first n rows
            for _ in range(n):
                next(reader)

            # Write remaining rows to output file
            for row in reader:
                writer.writerow(row)

# Call function to skip first 5 rows
skip_rows(input_file, output_file, 5)

print(f"First 5 rows deleted. Result saved in {output_file}.")

new_file = 'C:/Users/joeas/Downloads/new_output.csv'

def new_amount_column(output_file, new_file):
    # Input CSV file name
    input_file = output_file

    # Output CSV file name (with the added column)
    output_file = new_file

    # Function to add a column based on conditions from two other columns
    def add_column(input_file, output_file):
        with open(input_file, 'r', newline='') as f_input, open(output_file, 'w', newline='') as f_output:
            reader = csv.DictReader(f_input)
            fieldnames = reader.fieldnames + ['Amount']  # Add the new column to fieldnames
            writer = csv.DictWriter(f_output, fieldnames=fieldnames)
            writer.writeheader()

            # Iterate through each row and add the new column based on conditions
            for row in reader:
                # Example condition: if column1 equals 'A' and column2 equals 'B', set the new column to 'Condition Met'
                if row['De'] == 'A' and row['Column2'] == 'B':
                    row['New_Column'] = 'Condition Met'
                else:
                    row['New_Column'] = 'Condition Not Met'
                writer.writerow(row)

    # Call the function to add the new column
    add_column(input_file, output_file)

    print(f"New column added based on conditions. Result saved in {output_file}.")

new_amount_column(output_file, new_file)