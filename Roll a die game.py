import tkinter as tk
import random

def roll_die():
    result = random.randint(1, 6)
    if result == 1:
        message = "You rolled a 1 – Better luck next time!"
    elif result == 2:
        message = "You rolled a 2 – Not bad!"
    elif result == 3:
        message = "You rolled a 3 – Right in the middle."
    elif result == 4:
        message = "You rolled a 4 – Nice one!"
    elif result == 5:
        message = "You rolled a 5 – Great roll!"
    else:
        message = "You rolled a 6 – Excellent! Highest roll!"

    result_label.config(text=message)

# Create GUI window
window = tk.Tk()
window.title("Roll a Die Game")
window.geometry("400x200")
window.resizable(False, False)

# Create and place widgets
title_label = tk.Label(window, text="🎲 Roll a Die 🎲", font=("Arial", 18))
title_label.pack(pady=10)

roll_button = tk.Button(window, text="Roll the Die", font=("Arial", 14), command=roll_die)
roll_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI loop
window.mainloop()
