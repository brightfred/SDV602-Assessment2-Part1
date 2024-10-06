"""
main.py

This is the main file to run the Weather Data Application. 
It contains all the logic for the des (data entry screens) windows and the top command interface.
It imports functions from all the other modules

What this file does:
Creates the top command interface and des windows.
Handles user interaction(events) coming from the top command interface and des windows.
Navigation between screens(prev and next buttons).
Displays charts(plots) in the des windows.

References:
- PySimpleGUI documentation: https://pysimplegui.readthedocs.io/en/latest/
- Matplotlib documentation: https://matplotlib.org/stable/contents.html
"""

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import matplotlib.pyplot as plt

import current_condition.current_condition as current_condition  
import historical_data.historical_data as historical_data      
import yearly_comparison.yearly_comparison as yearly_comparison 
import top_command_interface.top_command_interface as top_command_interface  


def create_chart(window_index, window):
    """
    Create the chart for the selected window (DES).

    The function check which chart to create based on the window index.
    Then, it embeds the plot into the window.
    I get the key of the canvas to embed the plot.
    I aggregate the figure and draw the plot on the canvas.
    Similar to the example provided in example folder.
    I use canvas-chart as key to get the canvas for each window.

    Reference for figure_canvas_agg.get_tk_widget and figure_canvas_agg.draw: https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html
    
    """
    fig = None
    if window_index == 0:
        fig = current_condition.create_currentCondition_chart()
    elif window_index == 1:
        fig = historical_data.create_historical_chart()
    elif window_index == 2:
        fig = yearly_comparison.create_yearly_chart()

    canvas_elem = window['canvas-chart']  # this is my key to get the canvas for each window
    canvas = canvas_elem.TKCanvas      
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)  
    figure_canvas_agg.draw()                      
    figure_canvas_agg.get_tk_widget().pack()  
    return figure_canvas_agg


def main():
    """
    Main function of the application.

    Steps:
    I assign a variable to the top interface to ease the call of the function.
    Then i set the location of the des window and top interface.
    I create a list of windows_layout to store each des specific layouts from in each module.
    When a window is called, i get a layout from the list  as i iterate through the list(list comprehension) to get the right index(0,1,2).
    I hide all windows at the start using a for loop.

    
    Reference for PySimpleGUI Window: https://pysimplegui.readthedocs.io/en/latest/#window-class
    Reference for enumerate: https://docs.python.org/3/library/functions.html#enumerate
    Reference for read_all_windows: https://pysimplegui.readthedocs.io/en/latest/#multiple-windows
    Reference for sg.popup: https://docs.pysimplegui.com/en/latest/documentation/quick_start/popups_input_type/
    Reference for enumerate : https://www.w3schools.com/python/ref_func_enumerate.asp
    Reference for list comprehension: https://www.w3schools.com/python/python_lists_comprehension.asp
    Reference for len: https://www.w3schools.com/python/ref_func_len.asp
    """
    top_i = top_command_interface.create_top_interface()
    top_i.finalize()  
    top_i.CurrentLocation()  
    top_i.size      
    

    #List of all the des layout
    window_layouts = [
        current_condition.currentCondition_des_layout(),  
        historical_data.historical_des_layout(),          
        yearly_comparison.yearly_des_layout()             
    ]

    # i set a title for the window 
    # i set  location ,without it ,the window go off screen 
    windows = [
        sg.Window(
            'Weather App',      
            layout,             
            finalize=True,
            size=(1000, 1200),   #FIXME - i set the window size (doesnt really work ,it always shrink back)
            location=(500, 100), 
        )
        for i, layout in enumerate(window_layouts)
        # This one is tricky,i uses a list comprehension with enumerate.It allows me to get the right index in window_layouts list. 
    ]

    #hide all windows at the start
    for window in windows: 
        window.Hide()

    current_window_index = 0  

    figure_agg_list = [None, None, None]  # To store figure canvases for each window

    # I changed the for loop using range from the example in multiwindow.py.With this one,
    # i use the index to get the right figure_agg_list as in the example, it is not using a list.
    # A list made sense to me as i am dealing with multiple windows + a command interface.
    # the way it works is that it creates the chart for each window and stores it 
    # in the figure_agg_list.
    for i in range(len(windows)):
        figure_agg_list[i] = create_chart(i, windows[i])



    # Main function event loop to handle user interactions with all elements
    #while true means that the loop will run until the user closes the window
    #the way this loop works is that it waits for events from any window(top interface or des windows)
    #it then handles the events from the top command interface
    #it switches to the des window based on the event.Example : Current Condition, Historical Data, Yearly Comparison
    while True:
        window, event, values = sg.read_all_windows()  # Read events from all windows

        if window == top_i:
            # events from the top command interface
            if event == 'Current Condition':
                windows[current_window_index].Hide()
                current_window_index = 0
                windows[current_window_index].UnHide()

            elif event == 'Historical Data':
                windows[current_window_index].Hide()
                current_window_index = 1
                windows[current_window_index].UnHide()

            elif event == 'Yearly Comparison':
                windows[current_window_index].Hide()
                current_window_index = 2
                windows[current_window_index].UnHide()

            elif event == 'Exit' or event == sg.WIN_CLOSED:
                break  # Break out of the event loop similar to 



        elif window in windows: 
            # events from the des windows
            # I use len(windows) to get the lenght and use the modulo operator % only if i go over the lenght.if i stay in the range of the lenght,
            # i just go to the next window or the previous one.
            if event == 'Prev':
                windows[current_window_index].Hide()
                current_window_index = (current_window_index - 1) % len(windows)
                windows[current_window_index].UnHide()
            
            elif event == 'Next':
                windows[current_window_index].Hide()
                current_window_index = (current_window_index + 1) % len(windows)
                windows[current_window_index].UnHide()

            elif event == 'Fetch Weather':
                sg.popup('Logic will be implemented in V2 for Fetch Weather Button.') #FIXME - Add logic in V2 for the Fetch Weather button

            elif event == 'Send':
                sg.popup('Logic will be implemented in V2 for the Chat')  #FIXME - Add logic in V2 for the chat

            elif event == 'Exit' or event == sg.WIN_CLOSED:
                break  

if __name__ == '__main__':
    main()  