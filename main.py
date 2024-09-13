from tkinter import *
from tkinter.ttk import *
from layout import create_widgets

# Creating the window and giving it a title
root = Tk()
root.title("BMI Index Calculator")
root.frames = {}

# Setting the window size
# root.geometry('380x450')

# Trying the thing above but in a different way
initial = Frame(root, width=380, height=450) # after the height=450 i want to test out **, bg="")**, maybe a hex code? idk figure it out

# Scale it up so we can see it better
root.tk.call('tk', 'scaling', 2.25)

# Creating widgets
create_widgets(root)

# Needing to refresh it
root.mainloop()
