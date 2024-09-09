import tkinter as tk
import subprocess
import os

# Get the absolute path of the current directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Function to open Open Orders Reports menu
def open_orders_menu():
    open_orders_path = os.path.join(base_dir, 'oo_reports', 'oo_report_menu.py')
    subprocess.run(['python', open_orders_path])

# Function to open End of Day Reports menu
def eod_reports_menu():
    eod_reports_path = os.path.join(base_dir, 'eod_reports', 'eod_menu.py')
    subprocess.run(['python', eod_reports_path])

# GUI Setup
root = tk.Tk()
root.title("Main Menu")
root.geometry("300x250")  # Fixed window size (adjust the width and height as needed)

# Add Labels and Buttons for the Options
tk.Label(root, text="Choose a set of reports:", font=("Arial", 14)).pack(pady=20)

# Button to open the Open Orders Reports menu
tk.Button(root, text="Open Orders Reports", command=open_orders_menu).pack(pady=10, padx=50, anchor="center")

# Button to open the End of Day Reports menu
tk.Button(root, text="End of Day Reports", command=eod_reports_menu).pack(pady=10, padx=50, anchor="center")

# Exit Button
tk.Button(root, text="Exit", command=root.quit).pack(pady=10, padx=50, anchor="center")

# Add copyright label at the bottom
copyright_label = tk.Label(root, text="© 2024 @mr.fjfranco - All rights reserved.", font=("Arial", 8))
copyright_label.pack(side="bottom", pady=5)

# Start the Tkinter loop
root.mainloop()
