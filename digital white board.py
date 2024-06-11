from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk, filedialog, simpledialog, messagebox
import tkinter as tk
import os


root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'
eraser_mode = False

def locate_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def addLine(event):
    global current_x, current_y
    if not eraser_mode:
        canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=TRUE)
    else:
        canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(), fill='white', capstyle=ROUND, smooth=TRUE)
    current_x, current_y = event.x, event.y

def toggle_eraser_mode():
    global eraser_mode
    eraser_mode = not eraser_mode

def show_color(new_color):
    global color, eraser_mode
    color = new_color
    eraser_mode = False
# Define a function to clear the canvas
def clear_canvas():
    canvas.delete('all')
    display_palette()

# Create a button to clear the canvas
clear_button = Button(root, text="Clear Canvas", bg="#f2f3f5", command=clear_canvas)
clear_button.grid(row=0, column=4, padx=10, pady=10)  # Adjust row and column as needed

def save_canvas():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("Postscript files", "*.ps")])
        if file_path:
            canvas.postscript(file=file_path)
            convert_to_image(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the canvas: {e}")


def convert_to_image(ps_file_path):
    img_file_path = ps_file_path.replace('.ps', '.png')
    os.system(f"gswin64c -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -r144 -sOutputFile={img_file_path} {ps_file_path}")
    os.remove(ps_file_path)
    messagebox.showinfo("Save", f"Canvas saved as {img_file_path}")

def open_saved_file():
    file_path = filedialog.askopenfilename(defaultextension=".ps", filetypes=[("Postscript files", "*.ps")])
    if file_path:
        os.system(file_path)

# Icon
try:
    image_icon = PhotoImage(file="logo.png")
    root.iconphoto(False, image_icon)
except:
    pass

try:
    color_box = PhotoImage(file="color section.png")
    Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)
except:
    pass

try:
    eraser_img = PhotoImage(file="eraser.png")
    eraser_button = Button(root, image=eraser_img, bg="#f2f3f5", command=toggle_eraser_mode)
    eraser_button.place(x=30, y=400)
except:
    pass

colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((10, 280, 30, 300), fill='white')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

display_palette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value = tk.DoubleVar()

open_saved_button = Button(root, text="Open", bg="#f2f3f5", command=open_saved_file)
open_saved_button.grid(row=0, column=3, padx=10, pady=10)
save_button = Button(root, text="Save", bg="#f2f3f5", command=save_canvas)
save_button.grid(row=0, column=0, padx=10, pady=10)


save_button = Button(root, text="Save", bg="#f2f3f5", command=save_canvas)
save_button.grid(row=0, column=0, padx=10, pady=10)
clear_button = Button(root, text="Clear", bg="#f2f3f5", command=clear_canvas)
clear_button.grid(row=0, column=4, padx=10, pady=10)  # Adjust row and column as needed




def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()

