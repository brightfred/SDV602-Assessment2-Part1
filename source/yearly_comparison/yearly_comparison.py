import PySimpleGUI as sg
import matplotlib.pyplot as plt

"""
yearly_comparison.py

This module contains the "Yearly comparison" layout and the function to create the chart(line).
I use matplotlib to create the line chart and pysimplegui to create the layout.
"""



def yearly_des_layout():
    """
    Function to create the layout.
    The chatbox and chatinput are non-functional at the moment.Same for the fetch weather button.
    Reference for combo: https://docs.pysimplegui.com/en/latest/cookbook/original/keybad_entry/
    Reference for multiline: https://docs.pysimplegui.com/en/latest/documentation/module/elements/multiline/
    Reference for key: https://docs.pysimplegui.com/en/latest/cookbook/original/keybad_entry/
    Reference for push: https://docs.pysimplegui.com/en/latest/documentation/module/layouts/#push
    Reference for expand_x: https://docs.pysimplegui.com/en/latest/documentation/module/common_element_parameters/#expand_x-expand_y
    """
    figure_w, figure_h = 700, 400
    layout = [
        [sg.Button('Prev'), sg.Text('Yearly Comparison', font=('Arial', 22), justification='center', expand_x=True), sg.Button('Next')],
        [sg.Text('Data type:'),sg.Combo(['Temperature', 'Humidity', 'Pressure'],default_value='Temperature',)],
        [sg.Text('City:'), sg.Input(size=(20, 2))],
        [sg.Push(), sg.Text('Choose a year 1:'), sg.Input(size=(10, 2),), sg.Text(' VS '), sg.Text('Year 2:'), sg.Input(size=(10, 2)), sg.Push()],
        [sg.Canvas(size=(figure_w, figure_h), key='canvas-chart')],
        [sg.Push(), sg.Button('Fetch Weather', size=(20, 2)), sg.Push()],
        [sg.Multiline(size=(60, 5), expand_x=True)],
        [sg.Input(expand_x=True)],
        [sg.Push(), sg.Button('Send'),sg.Push()],
        [sg.Push(), sg.Button('Exit')],
    ]
    return layout

def create_yearly_chart():
    """
    This function create a double line chart about two chosen year of a specific data type.
    It is hardcoded at the moment with dummy data.

    #TODO - For V2:
    The ylabel of my chart should be dynamic. It should change according to the data type selected by the user.
    I will add more data type after looking at the openweather app api documentation and see what is available.
    The title name should be dynamic according to the years selected by the user and the data type
    (Example: Temperature in 2020 vs 2021 in Nelson).
    The label of my chart should also be dynamic. It should display the chosen years by the user.

    Reference for plt.subplots,ax.set and ax.plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
    """
    fig, ax = plt.subplots(figsize=(10, 4))  
    categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    values_year1 = [3, 7, 5, 9, 6, 8, 4, 7, 5, 10, 6, 8]
    values_year2 = [4, 6, 5, 8, 7, 9, 5, 6, 6, 9, 7, 7]

    ax.plot(categories, values_year1, label="year1")#This need to be fix as it isnt dynamic
    ax.plot(categories, values_year2, label="year2")  #This need to be fix as it isnt dynamic

    ax.set_title("Yearly Comparison")
    ax.set_ylabel("Data type")
    ax.set_xlabel("Months")
    ax.legend()  
    
    return fig
