from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# contrast border thumbnail
root = Tk()
root.title("Erlan's Photo Editor")
root.geometry("640x640")
root.iconphoto(True, PhotoImage(file="alatoo.png"))

# create functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1


def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1


def rotate_image(event):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas2.create_image(300, 210, image=img7)
    canvas2.image = img7



def filter():
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img8 = img.convert("1")
    img9 = ImageTk.PhotoImage(img8)
    canvas2.create_image(300, 210, image=img9)
    canvas2.image = img9

def resize_image(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = img.resize((int(resize_combo.get()), int(resize_combo.get())))
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image = img11

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None


def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            imgg.save(file)
        elif canvas2.image == img3:
            img2.save(file)
        elif canvas2.image == img5:
            img4.save(file)
        elif canvas2.image == img7:
            img6.save(file)
        elif canvas2.image == img9:
            img8.save(file)
        elif canvas2.image == img11:
            img10.save(file)
        # create labels, scales and comboboxes


blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=-50, y=30)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale1.place(x=100, y=35)

rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=350, y=30)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=440, y=35)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

resize = Label(root, text="Resize:", font=("ariel 17 bold"))
resize.place(x=350, y=90)
values1 = [140, 240, 360, 520, 720, 1080]
resize_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
resize_combo.place(x=440, y=97)
resize_combo.bind("<<ComboboxSelected>>", resize_image)

btn4 = Button(root, text="Black & White", bg='white', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=filter)
btn4.place(x=25, y=90)
# create canvas to display image
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2, bg= "grey")
canvas2.place(x=15, y=150)
# create buttons
btn1 = Button(root, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn1.place(x=50, y=595)
btn2 = Button(root, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=230, y=595)
btn3 = Button(root, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
              command=root.destroy)
btn3.place(x=430, y=595)
root.mainloop()