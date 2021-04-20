import csv
import requests
from collections import Counter

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)


juegos_gratis = []
todos_los_juegos = []
for linea in csvreader:
    if linea[7] == "0" and "ES" in linea[12]:
        juegos_gratis.append(linea[2])
        
    try:    # Hay juegos que no tienen rating
        linea[6] = int(linea[6])   
        todos_los_juegos.append(linea)
    except:
        linea[6] = linea[6] = 0
        todos_los_juegos.append(linea)
archivo.close()


ordenados = sorted(todos_los_juegos, key=lambda juego: int(juego[6]), reverse=True)

print(juegos_gratis)


for mejores in ordenados[0:10]:
    #print(mejores[0] + "   " + str(mejores[6]))
    print("Iconos de mejores juegos: ", mejores[4])

