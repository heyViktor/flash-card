from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    db = pandas.read_csv("used_words.csv")

except FileNotFoundError:
    db = pandas.read_csv("french_words.csv")

finally:
    flash_words = db.to_dict(orient="records")
    current_card = random.choice(flash_words)


def remove_card():
    flash_words.remove(current_card)
    next_card()

    data = pandas.DataFrame(flash_words)
    data.to_csv("used_words.csv", index=False)


def next_card():
    global flip_timer, current_card
    current_card = random.choice(flash_words)
    window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_image, image=flash_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=flash_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

flash_front = PhotoImage(file="images/card_front.png")
flash_back = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=flash_front)

language = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=current_card["French"], fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1,)

right_button = Button(image=right_image, highlightthickness=0, bd=0, command=remove_card)
right_button.grid(column=1, row=1)

window.mainloop()
