import tkinter as tk
import random
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Dice Roll Simulator")
window.geometry("300x400")
window.configure(bg="lightblue")    
window.resizable(False, False)

dice =["inverted-dice-1.png", "inverted-dice-2.png", "inverted-dice-3.png",
        "inverted-dice-4.png", "inverted-dice-5.png", "inverted-dice-6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#image_label = tk.Label(window, image=image1, bg="lightblue")

# Load images for dice faces
dice_images = [ImageTk.PhotoImage(Image.open(f"dice_{i}.png")) for i in range(1, 7)]
window.mainloop()