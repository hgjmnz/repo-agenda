import datetime
ahora = datetime.datetime.now()

import os

clear = lambda: os.system('clear')

import pandas as pd
info=[]
def agregar():
    persona=[]
    persona.append(input("Ingresar su Nombre: "))
    persona.append(input("ingresar su apellido: "))
    persona.append(input("ingrese su telefon: "))
    persona.append(input("ingrese correo electronico: "))
    persona.append(input("ingrese fecha de nacimiento: "))
    persona.append(input("ingrese usuario de instagram: "))
    persona.append(input("ingrese algun comentario: "))
    return persona


def consultar():
    for persona in info:
        print("Nombre: ",persona[0])
        print("Apellido: ",persona[1])
        print("Telefono: ", persona[2])
        print("Correo electronico: ", persona[3])
        print("Fecha de nacimiento: ",persona[4])
        print("Instagram: ", persona[5])
        print("Comenetario: ",persona[6])
        print("____________________________")

dtmp=pd.read_csv('contact.csv')
tmp=dtmp.values.tolist()
for lin in tmp:
    t=[]
    t.append(lin[1])
    t.append(lin[2])
    t.append(lin[3])
    t.append(lin[4])
    t.append(lin[5])
    t.append(lin[6])
    t.append(lin[7])
    info.append(t)

def modificar():
    posicion=input("ingrese la posicion en la que se encuentra el contacto")
    if posicion =="1":
        info[0]=agregar()
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')
    if posicion =="2":
        info[1]=agregar()
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')
    if posicion =="3":
        info[2]=agregar()
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')
    if posicion =="4":
        info[3]=agregar()
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')
    if posicion =="5":
        info[4]=agregar()
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')

def menu():
    clear()
    print("********************************************")
    print("*  Por favor elija una opcion del menu     *")
    print("*                                          *")
    print("*         1 - Agregar                      *")
    print("*         2 - Consultar                    *")
    print("*         3 - Modificar                    *")
    print("*         4 - Salir                        *")
    print(ahora.strftime("*             %d/%m/%Y %H:%M             *"))
    print("*                                          *")
    print("********************************************")
    opt=input("Inserte el valor: ")
    clear()
    if opt=="1":
        info.append(agregar())
        input("Se han guardado correctamente los contactos, presione enter para volver al menu")
        menu()
        clear()
    if opt=="2":
        consultar()
        input("estos son los contactos, presione enter para volver al menu")
        menu()
        clear()
    if opt=="3":
        modificar()
        input("Se han guardado correctamente los contactos, presione enter para volver al menu")
        menu()
        clear()
    if opt=="4":
        df = pd.DataFrame(info, columns=['nombre','apellido','telefono','correo electronico','fecha de nacimiento','instagram','comentario'])
        df.to_csv('contact.csv')
        
menu()

