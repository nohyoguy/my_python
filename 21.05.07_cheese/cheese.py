# -*- coding: utf-8 -*-
f = open("fucking_cheese.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line[:-1])
f.close()
