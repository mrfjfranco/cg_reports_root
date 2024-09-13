import csv
import requests
import tkinter as tk
from tkinter import messagebox

# Function to check the authorization in real-time
def check_authorization():
    # GitHub repository and file details
    github_csv_url = "https://raw.githubusercontent.com/mrfjfranco/authorization-check/main/auth.csv"
    
    try:
        # Fetch the file content from the GitHub raw URL
        response = requests.get(github_csv_url)
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.text}")

        response.raise_for_status()  # Ensure the request was successful
        csv_content = response.text.splitlines()

        # Parse the CSV content
        reader = csv.reader(csv_content)
        rows = list(reader)

        # Check if the first line matches the expected phrase
        expected_phrase = "FR@%c!$C0"  # Replace with your expected phrase
        if rows and rows[0][0] == expected_phrase:
            print("Authorization successful, continuing execution...")
        else:
            # Show the second line message in a messagebox and exit the program
            show_error_and_exit(rows[1][0] if len(rows) > 1 else "Authorization failed")

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



# Function to check the message from GitHub using the API
def check_message():
    # GitHub repository and file details
    owner = "mrfjfranco"
    repo = "message-check"
    file_path = "cg_reports_message.csv"
    api_url = f"https://raw.githubusercontent.com/mrfjfranco/message-check/main/cg_reports_message.csv"

    try:
        # Fetch the file content from the GitHub API
        response = requests.get(api_url)
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        response.raise_for_status()  # Ensure the request was successful
        csv_content=response.text.splitlines()

        # Check if the first line contains a message
        if csv_content and csv_content[0].strip():  # Ensures the first line is not empty
            message = csv_content[0].strip()
            show_message_popup(message)
        else:
            print("No message found, continuing as normal...")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}, continuing as normal...")

# Function to show the message in a pop-up window
def show_message_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Message", message)  # Show the message in a pop-up
    root.quit()  # Close the pop-up and return to the main program

