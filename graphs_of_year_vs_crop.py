# import required library
import pandas as pd # to read and store data
from matplotlib import pyplot as pt # to make graph
import tkinter as tk # to make input window
from tkinter import ttk # to easy our work

data = pd.read_csv("crop_production.csv") # read data from file

# function for graph plot
def Plot_graph(event):
    state_district_crop_data = state_district_data[state_district_data.Crop == slt_crop.get()] # saperate the data of selected crop from district data
    pt.figure(figsize=(14,7)) # size of graph window

    x_year = state_district_crop_data.Crop_Year # store year in saperate variable
    y_production = state_district_crop_data.Production # store production in saperate variable
    y_area = state_district_crop_data.Area # store area in saperate variable

    plot1 = pt.subplot() # to make y axis
    plot2 = plot1.twinx() # make other y axis
    plot1.plot(x_year, y_production, color="green", marker="o") # plot graph of year vs production
    plot1.set_ylabel("Production (in metric tons)", color="green", fontsize=18) # write label of 1st y axis
    plot2.plot(x_year, y_area,color="brown", marker="*") # plot graph of year vs area
    plot2.set_ylabel("Cultivation Area (in hectares)", color="brown", fontsize=18) # write label of 2nd y axis
    plot1.set_xlabel("Years", fontsize=15) # write label of x axis
    pt.title(slt_crop.get() + " production in " + slt_district.get() + ", " + slt_state.get()) # add title of graph
    pt.show() # display graph

# function to select state
def select_state():
    state_Name = sorted(data["State_Name"].unique().tolist()) # make the list of states present in given data
    tk.Label(window,text="Choose State", width=30).grid(row=0) # make the label for combobox and add location
    global slt_state # make global variable
    slt_state = ttk.Combobox(window, width=40) # make combobox and add size
    slt_state["value"] = state_Name # add the list of state to combobox
    slt_state.current() # add default value of combobox
    slt_state.grid(row=0, column=1) # location of combo box in window

    global state_button # make global variable
    state_button = tk.Button(window, text = "Click to select District", width=20) # make button
    state_button.grid(row=1,column=1) # location of button on window
    state_button.bind("<Button-1>", select_district) # call the fun(select_district) after the button clicked

# function to select district
def select_district(event):
    global state_data # make global variable
    state_data = data[data.State_Name == slt_state.get()] # saperate the data of selected state from raw data
    district_Name = sorted(state_data["District_Name"].unique().tolist()) # meke the list of district in selected state
    tk.Label(window,text="Choose District").grid(row=2) # make the label for combobox and add location
    global slt_district # make global variable
    slt_district = ttk.Combobox(window, width=40) # make combobox and add size
    slt_district["value"] = district_Name # add the list of district to combobox
    slt_district.current() # add default value of combobox
    slt_district.grid(row=2, column=1) # location of combo box in window

    global dist_button # make global variable
    dist_button = tk.Button(window, text = "Click to select Crop", width=20) # make button
    dist_button.grid(row=3,column=1) # location of button on window
    dist_button.bind("<Button-1>", select_crop) # call the fun(select_crop) after the button clicked

# function to select crop
def select_crop(event):
    global state_district_data # make global variable
    state_district_data = state_data[state_data.District_Name == slt_district.get()] # saperate the data of selected district from state data
    crops_name = sorted(state_data["Crop"].unique().tolist()) # make the list of crop grown in selected district
    tk.Label(window, text="Select Crop").grid(row=4) # make the label for combobox and add location
    global slt_crop # make global variable
    slt_crop = ttk.Combobox(window, width=40) # make combobox and add size
    slt_crop["value"] = crops_name # add list of crop to combobox
    slt_crop.current() # add default value of combobox
    slt_crop.grid(row=4, column=1) # location of combo box in window

    global crop_button # make global variable
    crop_button = tk.Button(window, text = "Click to See Graph", width=20) # make button
    crop_button.grid(row=5,column=1) # location of button on window
    crop_button.bind("<Button-1>", Plot_graph) # call the fun(Plot_graph) after the button clicked

# make window
window = tk.Tk() # make window
window.title("Crop production in india") # title of window
window.geometry("600x400") # size of window

select_state() # call the fun(select_state) to select the name of state

window.mainloop() # display window


# END

