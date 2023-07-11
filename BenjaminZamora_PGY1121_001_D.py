
import numpy as np
import os
depto=np.empty([10,4],type(int))
ruts=[]
def llenar(depto): 
    p=1
    for i in range(10):
        for j in range(4):
            depto[i,j]=p
            p+=1
def valiaOp():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp

def comprardepto(depto):
    tipo=""
    while(len(tipo)<=0):
        print("\n")
        print("Tipo A, 3.800 UF")
        print("Tipo B, 3.000 UF")
        print("Tipo C, 2.800 UF")
        print("Tipo D, 3.500 UF")
        tipo=input("elija el tipo de departamento que quiere comprar: ").upper()
        if(tipo!="A" and tipo!="B" and tipo!="C" and tipo!="D"):
            print("Debe ingresar una opcion correcta")
            tipo=""
    while(True):
        try:
            num=int(input("ingrese numero que desea de departamento: "))
            if(num>0 and num<40):
                break
        except ValueError:
            print("ingrese un numero de departamento valido")
    while (True):
        try:
            rut=int(input("ingrese su rut minmo 9 digitos y sin puntos ni guion: "))
            if(rut<=999999999):
                break
        except ValueError:
            print("ingrese un rut correcto")
    ruts.append(rut)
    if tipo=="A":
        pago= 3800
    if tipo=="B":
        pago=3000
    if tipo=="C":
        pago=2800
    if tipo=="D":
        pago=3500
    for i in range(10):
        for j in range(4):
            if(num==depto[i,j]):
                
                depto[i,j]="X"
    print("la compra fue realizada de forma exitosa")
    os.system("pause")
    return pago 
def Listado(ruts):
    ruts.sort()
    print("Listado de compradores de deptos ordenados de menor a mayor ")
    print("\t",ruts)
def venta(depto):
    for i in range(10):
        for j in range(4):
            contador=0
            recaudacion=0
            if(j==0):
                contador0=0
                if depto[i,j]=="X":
                    contador0+=1
                    contador+=1
                    pagoa=3800*contador0
                    recaudacion+=pagoa
                    print(" el tipo de departamento A los compraron",contador0,"la recaudacion de tipo A es: ",pagoa)
            if(j==1):
                contador1=0
                if depto[i,j]=="X":
                    contador+=1
                    contador1+=1
                    pagob=3000*contador1
                    recaudacion+=pagob
                    print(" el tipo de departamento B los compraron",contador1,"la recaudacion de tipo B es: ",pagob)
            if(j==2):
                contador2=0
                if depto[i,j]=="X":
                    contador+=1
                    contador2+=1
                    pagoc=2800*contador2
                    recaudacion+=pagoc
                    print(" el tipo de departamento C los compraron",contador2,"la recaudacion de tipo C es: ",pagoc)
            if(j==3):
                contador3=0
                if depto[i,j]=="X":
                    contador+=1
                    contador3+=1
                    pagod=3500*contador3
                    recaudacion+=pagod
                    print(" el tipo de departamento D los compraron",contador3,"la recaudacion de tipo D es: ",pagod)
def mostrarDisponibles(depto):
    print(" \t" "A""\t""B""\t""C""\t""D""\t")
    for i in range(10):
        print("\n")
        for j in range(4):
            print("\t",depto[i,j], end="  ")
    print("\n")   
llenado=llenar(depto)
op=0
suma=0
while(op!=5):
    os.system("cls")
    print("     CASA FELIZ      ")
    print("     **********************     ")
    print(" 1.  Comprar departamento ")
    print(" 2.  Mostrar departamento disponible ")
    print(" 3.  Ver listado de compradores  ")
    print(" 4.  Mostrar ganacias totales ")
    print(" 5.  Salir  ")
    op=valiaOp()
    if(op==1):
        mostrar=mostrarDisponibles(depto)
        comprar=comprardepto(depto)
    if(op==2):
        mostrar=mostrarDisponibles(depto)
        os.system("pause")
    if(op==3):
        lista=Listado(ruts)
        os.system("pause")
    if(op==4):
        vendidos=venta(depto)
        os.system("pause")
    if(op==5):
        print("adios que esten bien, Benjamin Zamora, 11/07/2023")
        break

        
        




       

