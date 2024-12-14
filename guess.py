import tkinter as tk
from tkinter import messagebox
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

def check_guess():
    """Check the user's guess against the random number."""
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            messagebox.showinfo("Hint", "Please enter a number between 1 and 100.")
        elif guess < random_number:
            messagebox.showinfo("Hint", "Too low! Try again.")
        elif guess > random_number:
            messagebox.showinfo("Hint", "Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            reset_game()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def reset_game():
    """Reset the game with a new random number."""
    global random_number
    random_number = random.randint(1, 100)
    entry.delete(0, tk.END)

# Create main application window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x200")

# Instruction label
instruction = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
instruction.pack(pady=10)

# Entry field for user's guess
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check", font=("Arial", 14), command=check_guess)
check_button.pack(pady=5)

# Reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.pack(pady=5)

# Run the application
root.mainloop()
