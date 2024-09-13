# functions.py
def btnEnter_clicked(spin_box_system, height, weight):
    selected_option = spin_box_system.get()
    if selected_option == spin_box_system['values'][0]:

        height_value = height.get()
        print("Height: ", height_value)

        weight_value = weight.get()
        print("Weight: ", weight_value)
    # Perform actions based on the selected option()
