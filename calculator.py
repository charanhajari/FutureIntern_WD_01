import tkinter as tk
from tkinter import messagebox

def press_key(key):
    """Handles button presses by updating the input field."""
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Create main application window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Create an input field
entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: press_key(t))
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Configure rows and columns to scale with window size
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
