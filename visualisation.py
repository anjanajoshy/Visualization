# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:29:10 2023

@author: anjana
"""

import pandas as pd
import matplotlib.pyplot as plt

"""Creating functions for lineplot, piechart and barchart"""

"""Creating a line graph to represent the population's access to electricity"""

def lineplot(data_ele , country):
    data_1 = data_ele #data_ele is stored in new variable
    print(data_ele) #printing data_1
    plt.figure(figsize = (6,6)) #mentioning the size of figure
    #iterating over a row
    for x in country:
        plt.plot(data_1["Year"], data_1[x],label = x) 
    plt.xlim(2006,2025) #setting limit  for x-axis
    #xticks sets the x-axis tick value
    plt.xticks(data_1["Year"],labels = data_1["Year"], rotation = 'vertical')
    plt.title("Access to electricity")#setting title for graph
    plt.xlabel("YEAR") #labelling x-axis
    plt.ylabel("Percent of population") #labelling y-axis
    plt.legend()
    #saving figure as Access to electricity_lineplot
    plt.savefig("Access to electricity_lineplot.png")
    plt.show() 
    return #return statement is used to end tht execution of the function


if __name__ == "__main__":
    #Reading a dataset value in excel form for lineplot
    data_ele = pd.read_excel("Data_Extract_FromWorld_development.xlsx")
    
    #calling lineplot function
    lineplot(data_ele, ["Ethiopia","Kenya", "Angola","Comoros"] )