#!/usr/bin/env python3
#program to automate the creation of graphs given files of data
import sys
import matplotlib.pyplot as plt 
from itertools import cycle
import os
colors = ['g','r', 'b', 'c', 'm', 'y', 'k']

y_array = []
x_array = []

directory = os.listdir(os.getcwd())
data = []
#checks current directory to see if there are any files marked as data for the graph
for file1 in directory:
    if "STM" in file1: 
        data.append(file1)
count = 0
for i in data:
    x_values = []
    y_values = []
    with open(i, "r") as file1:
         f_list = [float(i) for line in file1 for i in line.split(',') if i.strip()]
         #if there is data on the line then it will split it by a comma and enter the numbers in as a float value for all lines

    for index, element in enumerate(f_list):
        if index % 2 == 0:
            x_values.append(int(element))
        else:
            y_values.append(element)
    x_array.append(x_values)
    y_array.append(y_values)
    plt.plot(x_array[count],y_array[count],c=colors[count%len(colors)],label=i)  
    count += 1

# ./grapher 3 input.txt input2.txt input3.txt

# function to show the plot 
plt.legend()
plt.savefig('graph.png')
plt.xlabel("Iterations")
plt.ylabel("Time(10^-2)")
plt.show()
file1.close()
