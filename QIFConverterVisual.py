import csv
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import time

def csv_to_qif(csv_file, qif_file, progress_bar, convert_button):
    with open(csv_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        total_rows = sum(1 for row in csv_reader)
        csv_file.seek(0)  # Reset file pointer
        
        next(csv_reader)
        
        with open(qif_file, 'w') as qif_file:
            qif_file.write('!Type:Bank\n')  # Set the type of data (Bank transactions)
            progress = 0
            
            for i, row in enumerate(csv_reader, 1):
                
                amount = -float(row['Amount'])
                
                qif_file.write('D{}\n'.format(row['Transaction date']))  # Date
                qif_file.write('T{}\n'.format(str(amount)))  # Amount
                qif_file.write('P{}\n'.format(row['Description']))  # Payee
                qif_file.write('M{}\n'.format(row['Category']))  # Memo
                qif_file.write('^\n')  # End of record
                
                progress = int((i / total_rows) * 100)
                progress_bar['value'] = progress
                progress_bar.update()
                time.sleep(0.05)  # Simulate processing time
                
    messagebox.showinfo("Conversion Completed", "CSV to QIF conversion completed successfully!")
    convert_button.config(state="normal")  # Enable the Convert button after conversion

def browse_csv():
    csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_path:
        entry_csv.delete(0, tk.END)
        entry_csv.insert(0, csv_path)
        entry_qif.insert(0, csv_path.replace(".csv", ".qif"))

def convert_to_qif():
    csv_file = entry_csv.get()
    qif_file = entry_qif.get()
    
    if not csv_file or not qif_file:
        messagebox.showerror("Error", "Please select CSV and QIF files.")
        return
    
    button_convert.config(state="disabled")  # Disable the Convert button during conversion
    progress_bar['value'] = 0
    progress_bar.update()
    csv_to_qif(csv_file, qif_file, progress_bar, button_convert)

# Create a tkinter window
root = tk.Tk()
root.title("CSV to QIF Converter")

# Label for CSV file entry
label_csv = tk.Label(root, text="CSV File:")
label_csv.grid(row=0, column=0)

# Entry field for CSV file
entry_csv = tk.Entry(root, width=50)
entry_csv.grid(row=0, column=1)

# Browse button for CSV file
button_browse_csv = tk.Button(root, text="Browse", command=browse_csv)
button_browse_csv.grid(row=0, column=2)

# Label for QIF file entry
label_qif = tk.Label(root, text="QIF File:")
label_qif.grid(row=1, column=0)

# Entry field for QIF file
entry_qif = tk.Entry(root, width=50)
entry_qif.grid(row=1, column=1)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_to_qif)
button_convert.grid(row=2, column=1)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=3, columnspan=3, pady=10)

# Run the tkinter event loop
root.mainloop()
