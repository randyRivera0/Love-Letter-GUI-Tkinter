import os
import tkinter as tk
from PIL import Image, ImageTk

# Constants
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")
IMAGES = [Image.open(os.path.join(IMAGE_FOLDER, f"pixil-frame-{i}.png")).convert("RGBA") for i in range(5)]
TEXT = 'Disfruto tu compañía, me alegra pasar tiempo contigo y encuentro encantadora tu vivacidad. Conocerte ha sido una experiencia maravillosa; aunque nos hubiera gustado tener más tiempo juntos, cada momento ha sido especial y de calidad. Te quiero ❤️'
BACKGROUND_IMAGE = os.path.join(IMAGE_FOLDER, "background.jpg")
BESITOS_CHICHIS_IMAGE = os.path.join(IMAGE_FOLDER, "besitos_chichis.png")


# Create the functions
def on_closing(window):
    open_image_window(window)
    window.withdraw()

def update_label_text(index=0):
    if index < len(TEXT):
        label3.config(text=TEXT[:index+1] + "_")
        label3.after(150, update_label_text, index+1)

def open_image_window(window):
    image_window = tk.Toplevel(window)
    image_window.title("Love you (kisses)")

    image = tk.PhotoImage(file=BESITOS_CHICHIS_IMAGE)
    label = tk.Label(image_window, image=image)
    label.image = image  # Prevent garbage collection
    label.pack()

def transition_photos(index=0):
    img = IMAGES[index]
    img_tk = ImageTk.PhotoImage(img)

    label2.config(image=img_tk)
    label2.image = img_tk

    index = (index + 1) % len(IMAGES)
    label2.after(500, transition_photos, index)

# Create the root
root = tk.Tk()
root.title("Dulzura en python")
root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

# Background
bg = Image.open(BACKGROUND_IMAGE).convert("RGBA")
bg_tk = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg_tk)
bg_label.place(x=0, y=0)

label1 = tk.Label(root, text='Con carino y mimos ❤️', font=("Helvetica", 20), fg="white", bg="pink")
label1.pack()

label2 = tk.Label(root, width=100, height=100, bg="#FFEBF0")
label2.pack(padx=25, pady=25)

label3 = tk.Label(root, text="", font=("Helvetica", 20), fg="white", bg="pink", justify="left", wraplength=500)
label3.pack()

# Start animation
transition_photos()
update_label_text()

root.mainloop()
