import random
import time
class carro:
    def __init__(self,ruedas=4,farolas=2):
        self.ruedas=ruedas
        self.farolas = farolas
    def potencia(self):
        potencia=self.ruedas*2+self.farolas
        if self.ruedas<0:
            self.ruedas=0
        if self.farolas<0:
            self.farolas=0
        if potencia==0:
            self.farolas=1
        return potencia
    def choque(self,tipo):
        
        if tipo==1:
            self.ruedas//=2
            self.farolas//=2
        elif tipo==2:
            self.farolas-=1
        elif tipo==3:
            self.ruedas-=1
        elif tipo ==4:
            self.ruedas=4
            self.farolas=2
        

def generarPista(carriles,tamaño):
    p=[["_" for i in range(tamaño)] for i in range(carriles)]
    return p   
        
def objetos(pista,objeto,cant):
    for i in range(cant):
        fila=random.randint(0,len(pista)-1)
        columna =random.randint(0,len(pista[0])-1)
        pista[fila][columna]=objeto
    return pista
def carrera(n,tam):
    ganador =None
    c=[0 for i in range(n)]
    carros=[carro() for i in range(n)]
    l=objetos(objetos(objetos(objetos(generarPista(n,tam),"|ª",2),"..",4),"O",3),"t",2)
    while ganador == None :
        mensaje =""
        p=""
        for i in range(n):
            limite=c[i]-carros[i].potencia()
            if limite<0:
                limite=0
            for j in range(limite,c[i]):
                
                if l[i][j]=="O":
                    carros[i].choque(1)
                    mensaje+="se ha dañado con un hueco el carro "+str(i)+";"
                elif l[i][j]=="|ª":
                    carros[i].choque(2)
                    mensaje+="se ha chocado contra 1 poste el carro "+str(i)+":"
                elif l[i][j]=="..":
                    carros[i].choque(3)
                    mensaje+="se ha pinchado una rueda con una puntilla el carro "+str(i)+";"
                
                elif l[i][j]=="t":
                    carros[i].choque(4)
                    mensaje+="se ha curado en un taller el carro "+str(i)+";"
            p+=str("".join(l[i][0:c[i]])+ "["+str(i)+"]"+"\n")
            c[i]+=carros[i].potencia()
            
            if c[i]>=tam and ganador==None:
                ganador=i
        print(p)
        print(str([i.potencia() for i in carros]),mensaje)
        time.sleep(0.5)
    print("el ganador es el auto ", ganador, "con un recorrido de ",c[ganador])
#aqui se escoje cuantos carros compiten y tambien el tamaño de la pista
carrera(4,109)








