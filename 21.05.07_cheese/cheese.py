# -*- coding: utf-8 -*-
f = open("fucking_cheese.txt", 'r')
lines = f.readlines()
f.close()

width = len(lines[0][:-1])
hight = len(lines)

cheese_list = []
cell_list = []
for i in range(width+2):
    cell_list.append('3')
cheese_list.append(cell_list)

for i in range(hight):
    cell_list = ['3']
    for j in range(width):
        cell_list.append(lines[i][j])
    cell_list.append('3')
    cheese_list.append(cell_list)

cheese_list.append(cheese_list[0])

for component in cheese_list:
    print(component)
