# Dice Roll Simulator with GUI using Tkinter
#This program simulates rolling two dice and displays the result with sound effects and animations.
import tkinter as tk
import random
from PIL import Image, ImageTk
from playsound import playsound
import threading

# Function to load and resize dice images
def load_resized_image(path, size=(150, 150)):
    img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Dice image files
dice = ["inverted-dice-1.png", "inverted-dice-2.png", "inverted-dice-3.png",
        "inverted-dice-4.png", "inverted-dice-5.png", "inverted-dice-6.png"]

# Setup window
window = tk.Tk()
window.title("Dice Roll Simulator")
window.geometry("500x350")
window.configure(bg="lightblue")

# Load initial dice images
image1 = load_resized_image(random.choice(dice))
image2 = load_resized_image(random.choice(dice))

# Dice labels
label1 = tk.Label(window, image=image1, bg="lightblue")
label1.image = image1
label1.place(x=100, y=80)

label2 = tk.Label(window, image=image2, bg="lightblue")
label2.image = image2
label2.place(x=280, y=80)

# Score and result labels
score_label = tk.Label(window, text="Total: 0", bg="lightblue", font=("Arial", 14, "bold"))
score_label.place(x=200, y=250)

result_label = tk.Label(window, text="", bg="lightblue", font=("Arial", 12, "bold"))
result_label.place(x=150, y=290)

# Function to play sound in a separate thread
def play_sound_async(sound_file):
    threading.Thread(target=playsound, args=(sound_file,), daemon=True).start()

# Roll dice function
def roll_dice():
    play_sound_async("roll.mp3")  # Play sound in a separate thread

    # Update dice images multiple times for animation effect
    for _ in range(10):  # You can adjust the range for faster/slower animation
        dice1 = random.choice(dice)
        dice2 = random.choice(dice)

        new_image1 = load_resized_image(dice1)
        new_image2 = load_resized_image(dice2)
        label1.configure(image=new_image1)
        label1.image = new_image1
        label2.configure(image=new_image2)
        label2.image = new_image2

        window.update_idletasks()  # Update the window
        window.after(50)  # Delay between image changes (adjust for speed)

    # After animation, roll dice and show result
    dice1 = random.choice(dice)
    dice2 = random.choice(dice)

    new_image1 = load_resized_image(dice1)
    new_image2 = load_resized_image(dice2)
    label1.configure(image=new_image1)
    label1.image = new_image1
    label2.configure(image=new_image2)
    label2.image = new_image2

    # Extract number from filename
    num1 = int(dice1.split("-")[-1].split(".")[0])
    num2 = int(dice2.split("-")[-1].split(".")[0])
    total = num1 + num2
    score_label.config(text=f"Total: {total}")

    # Winning / Encouragement logic
    if num1 == num2:
        if num1 == 1:
            result_label.config(text="🎉 Snake Eyes! You Win!", fg="green")
            play_sound_async("win.mp3")
        elif num1 == 6:
            result_label.config(text="🎉 Boxcars! You Win!", fg="green")
            play_sound_async("win.mp3")
        else:
            result_label.config(text="🎉 Double Match! You Win!", fg="green")
            play_sound_async("win.mp3")
    elif total in [7, 11]:
        result_label.config(text=f"🎉 Lucky {total}! You Win!", fg="green")
        play_sound_async("win.mp3")
    elif total in [2, 12]:
        result_label.config(text="🎉 Snake Eyes or Boxcars! You Win!", fg="green")
        play_sound_async("win.mp3")
    elif num1 == 1 or num2 == 1 :
        result_label.config(text="🍀 Good Luck! You got a 1 or 6 — Better chance next roll!", fg="blue")
        play_sound_async("encouragement.mp3")
    elif num1 == 6 and num2 == 6:
        result_label.config(text="🎉 Double Six! You Win!")
        play_sound_async("win.mp3")
    else:
        result_label.config(text="😢 Try Again!", fg="red")
        play_sound_async("lose.mp3")

# Roll button
button = tk.Button(window, text="Roll Dice 🎲", command=roll_dice,
                   bg="lightgreen", font=("Arial", 14, "bold"))
button.place(x=190, y=20)

window.mainloop()

