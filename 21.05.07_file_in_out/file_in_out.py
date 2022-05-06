# -*- coding: utf-8 -*-
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line[:-1])
f.close()
