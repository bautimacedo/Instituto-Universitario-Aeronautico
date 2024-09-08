#El archivo adjunto contiene temperaturas máximas y mínimas de los últimos 365 días para diferentes estaciones meteorológicas del Servicio
# Meteorológico Nacional (SMN). Construya un programa en Python que lee los datos del archivo y los coloca en un diccionario cuyas claves son
# los nombres de las estaciones meteorológicas. El valor asociado a cada clave debe ser otro diccionario con claves "tmax" y "tmin" que mapean con una lista de temperaturas.
#Si no se encuentra registrada una temperatura se la almacenará con el valor None.
#Una  vez cargados los datos se debe hacer un reporte por estación meteorológica de la temperatura máxima y mínima registrada en el período de 1 año.
#Ej.: Si quiero saber la temperatura mínima de Córdoba hace 3 días atrás debo accederla de la siguiente forma
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


estaciones= {}
archivo = open("C:/Users/bauti/OneDrive/Desktop/IUA/3er Año/DHS/Registro_temperaturas-02092024/temperaturas.txt","r")
for linea in archivo:
    partes = linea.strip().split()

    if es_numero(partes[1]) and es_numero(partes[2]):
        tmax=partes[1]
        tmin=partes[2]
        nombre=" ".join(partes[3:]) # uso [3:] porque puede tener dos palabras el nombre entonces lo une
        if(tmax==" "):
            tmax=None
        if(tmin==" "):
            tmin=None
            if nombre not in  estaciones: #Cuando no esta el nombre de la estacion, lo agrega como CLAVE, y el VALOR es un diccionario que tiene como clave tmax y tmin y los valores son listas
                estaciones[nombre]={"tmax":[], "tmin":[]}
            estaciones[nombre]["tmax"].append(tmax)
            estaciones[nombre]["tmin"].append(tmin)
    else:
        print("FF")
