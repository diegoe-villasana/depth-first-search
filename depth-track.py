import numpy as np
import pandas as pd

def laberintos(dimensiones, muros):
    laberinto=[]
    for i in range(dimensiones):
        fila=[]
        for j in range(dimensiones):
            if tuple([i,j]) in muros:
                fila.append("#")
            else:
                fila.append(" ")
                fila.append(" ")
        laberinto.append(fila)
    return laberinto

print("hola")
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
lab = laberintos(5, muro)
for i in lab:
    print(''.join(i))

