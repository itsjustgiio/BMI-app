from tkinter import *
from tkinter.ttk import *
from functions import *

def create_widgets(root):
    # Creating a Label Widget
    myLabel = Label(root, text="Metric(kg) or Imperial(lbs)?")
    myLabel.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # Blank space
    blankspace = Label(root, text="")

    # Buttons for Metric or Imperial
    #btnMetric = Button(root, text="Metric")
    #btnMetric.grid(column=0, row=2, pady=10)

    #btnImperial = Button(root, text="Imperial")
    #btnImperial.grid(column=1, row=2, pady=10)

    # Example Spinbox with predetermined values (commented out)
    system = ("Imperial", "Metric")
    spin_box_system = Combobox(root, values=system, font=("Helvetica",12))
    spin_box_system.grid(column=(0), row=(2), columnspan= 2, pady=10)

    #setting a defualt value in combo box
    #spin_box_system.current(0)

    # Box for collecting weight and height
    heightquestion = Label(root, text="Enter your Height:")
    heightquestion.grid(column=0, row=4, pady=10)

    height = IntVar()  # Use IntVar for height
    heightNumber = Spinbox(root, from_=0, to=999, textvariable=height)
    heightNumber.grid(column=1, row=4, pady=10)

    blankspace.grid(column=1, row=5, columnspan=2)

    weightquestion = Label(root, text="Enter your Weight:")
    weightquestion.grid(column=0, row=6)

    weight = IntVar()  # Use IntVar for weight
    weightNumber = Spinbox(root, from_=0, to=999, textvariable=weight)
    weightNumber.grid(column=1, row=6)

    btnEnter = Button(root, text="Enter", command=lambda: btnEnter_clicked(spin_box_system, height, weight))  # Pass spin_box_system as argument
    btnEnter.grid(column=0, row=7, columnspan=2, pady=10, padx=10)

    # Example Spinbox with predetermined values (commented out)
    # names = ("John", "Gio", "Juan", "Luis", "etc")
    # spin_box_example = Spinbox(root, values=names, font=("Helvetica", 20))
    # spin_box_example.grid(column=(example), row=(example))
