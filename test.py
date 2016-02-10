import math
import random 


header = """P3
500 500 255 
"""
xres = 500
yres = 500
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

for i in range(1, xres+1):
    for j in range(1, yres+1):
        r = i**2/j**2 %255
        g = j**i %255
        b = i**j % 255
        header += str(r)+" "+str(g)+" "+str(b)+" "

f = open("test.ppm", "w")
f.write(header)
f.close()


