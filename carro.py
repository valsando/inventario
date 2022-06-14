'''Se trata de elaborar un programa Orientado a Objetos para simular una 
carrera de hasta 4 carros. Cada carro tiene potencia inicial 10, sus cuatro 
ruedas y dos farolas. La pista de 100 casillas es recorrida por cada carro
utilizando para avanzar un dado especial cuyo número de caras corresponderá
a la potencia del carro. A lo largo de la pista se deben distribuir
aleatoriamente 2 huecos, 4 postes y 3 puntillas, un hueco hará que el carro
quede con la mitad de su potencia actual, un poste quebrará una farola y
se pierde un punto de potencia, una puntilla pincha una rueda perdiendo 2
puntos de potencia (la potencia mínima es de 1), también en la pista se
deben colocar 3 talleres que harán que el carro recupere todas sus
características y toda su potencia.  Ganará el primer vehículo en llegar
a la meta (casilla 100)'''

import time
import os
import random

def mostrar_auto(cantidad_espacios):
    print(cantidad_espacios*" "," _________")
    print(cantidad_espacios*" ","|         \__")
    print(cantidad_espacios*" "," --0-----0---")

interaciones1=1
interaciones2=1 

while interaciones1<100 and interaciones2<100:
        os.system("cls")
        interaciones1=interaciones1+random.randint(0,3)
        interaciones2=interaciones2+random.randint(0,3)
        mostrar_auto(interaciones1)
        mostrar_auto(interaciones2)
        time.sleep(0.05)

if interaciones1>interaciones2:
    print("el ganador es el carro 1")
else:
    print("el ganador es el carro 2")

