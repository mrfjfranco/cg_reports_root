import csv
import requests
import tkinter as tk
from tkinter import messagebox

# Function to check the authorization
def check_authorization():
    # Replace with your GitHub raw file URL
    github_csv_url = "https://raw.githubusercontent.com/mrfjfranco/authorization-check/main/auth.csv"
    
    try:
        # Fetch the CSV content from the URL
        response = requests.get(github_csv_url)
        response.raise_for_status()  # Ensure the request was successful
        csv_content = response.text.splitlines()

        # Parse the CSV content
        reader = csv.reader(csv_content)
        rows = list(reader)

        # Check if the first line matches the expected phrase
        expected_phrase = "FR@%c!$C0"  # Replace with your expected phrase
        if rows[0][0] == expected_phrase:
            print("Authorization successful, continuing execution...")
        else:
            # Show the second line message in a messagebox and exit the program
            show_error_and_exit(rows[1][0])

    except Exception as e:
        show_error_and_exit(f"Failed to check authorization: {str(e)}")

# Function to display an error and exit the program
def show_error_and_exit(message):
    # Create a root window just for the error message box
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showerror("Authorization Failed", message)
    root.destroy()
    exit()  # Exit the program

# Call the authorization check when the program starts
check_authorization()
