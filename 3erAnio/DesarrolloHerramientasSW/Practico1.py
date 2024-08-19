1. #Crear un programa que contenga las siguientes funciones
# generardatos(n) que devuelve una lista de n numeros entero aleatorios entre 0 y 100
# guaurdardatos(nombre,datos) que guarda lo elementos de una lista en un archivo (uno por renglon)

import random

def generarDatos(n):
    lista= []
    for i in range(n):
        numero = random.randint(0, 100)
        lista.append(numero)
    return lista

def guardarDatos(nombre,lista):
    archivo=open(nombre,"w")
    for i in lista:
        archivo.write(str(i))
        archivo.write("\n")

datos = generarDatos(10)
nombre = "ArchivoPrueba.txt"
guardarDatos(nombre,datos)

2.#Crea un programa que contenga las funcioens
#leerdatos(nombre) que lee los datos contenidos en un archivo
#convertirdatos(entrada) que transforma los datos leidos del archivo en una lista de enteros
#convertirdatosLambda(entrada) que transofrma los daos leidos del acrhivo en una lista de enteros mediante listas por comprension
#noRepetidos(datos) que devuelve una lista de los elementos no repetidos (no usar for-in)

#Ejercicio 1
def leerDatos(file):
    with open(file,"r") as archivo:
        return archivo.read()

nombre = "ArchivoPrueba.txt"
contenido = leerDatos(nombre)


#Ejercicio 2
def convertirDatos(entrada):
    datos = list(entrada.split()) #Agrega pero string
    return datos
contenido2 = convertirDatos(contenido)
print(contenido2)

#Ejercicio 3

def convertir_entero(n):
    try:
        return int(n)
    except:
        return None

def convertirDatosLambda(entrada):
    datos = [int(i) for i in entrada if convertir_entero(i) is not None]
    print(datos)
convertirDatosLambda(contenido)

#Ejercicio 4

def noRepetidos(entrada):
    datos = [int(i) for i in entrada if convertir_entero(i) is not None]
    datos_unicos = set(datos)
    print(datos_unicos)
noRepetidos(contenido)
