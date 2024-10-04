import PySimpleGUI as sg

"""
top_command_interface.py

This module contains the code for the top command interface layout.
I only use simplegui librairy in this file to create the layout.
"""


def create_top_interface():
    """
    Function to create the top command interface(And layout).
    Reference for expand_x: https://docs.pysimplegui.com/en/latest/documentation/module/common_element_parameters/#expand_x-expand_y
    Reference for location: https://docs.pysimplegui.com/en/latest/call_reference/tkinter/window/
    Reference for push: https://docs.pysimplegui.com/en/latest/documentation/module/layouts/#push
    Reference for sg.window: https://docs.pysimplegui.com/en/latest/call_reference/#window
    https://docs.pysimplegui.com/en/latest/documentation/what_is_it/window_creation/#creating-the-window
    """
    layout = [
        [sg.Text('Weather Data App', font=('Arial', 20), justification='center', expand_x=True)],
        [sg.Push(),sg.Button('Current Condition', size=(20, 2), font=('Arial', 14)),sg.Push()],
        [sg.Push(),sg.Button('Historical Data', size=(20, 2), font=('Arial', 14)),sg.Push()],
        [sg.Push(),sg.Button('Yearly Comparison', size=(20, 2), font=('Arial', 14)),sg.Push()],
        [sg.Push(),sg.Button('Exit', size=(10, 2), font=('Arial', 14)),sg.Push()]
    ]
    top_command_interface_window = sg.Window(
        'Top Command Interface',
        layout,
        size=(300, 400),
        location=(None, None),  
    )
    return top_command_interface_window
