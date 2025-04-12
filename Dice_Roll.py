import tkinter as tk
import random
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Dice Roll Simulator")
window.geometry("500x360")
window.configure(bg="lightblue")    
window.resizable(False, False)

dice =["inverted-dice-1.png", "inverted-dice-2.png", "inverted-dice-3.png",
        "inverted-dice-4.png", "inverted-dice-5.png", "inverted-dice-6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Create a label to display the image of the dice
image_label = tk.Label(window, image=image1, bg="lightblue")
# image_label.pack(pady=20)
image_label2 = tk.Label(window, image=image2, bg="lightblue")
# image_label2.pack(pady=20)

# Create a button to roll the dice
image_label=tk.Label(window,image=image1,bg="lightblue")
image_label2=tk.Label(window,image=image2,bg="lightblue")



image_label.image=image1
image_label2.image=image2

# Load images for dice faces
# dice_images = [ImageTk.PhotoImage(Image.open(f"dice_{i}.png")) for i in range(1, 7)]
window.mainloop()