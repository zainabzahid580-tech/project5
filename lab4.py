import tkinter as tk

def change_color():
    background_color = button.cget("background")
    if background_color == "red":
        button.config(background="green")
    else:
        button.config(background="red")

window = tk.Tk()
button = tk.Button(window, text="click", command=change_color)
button.pack()
window.mainloop()