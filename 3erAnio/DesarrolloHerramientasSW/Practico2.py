import datetime

#El archivo adjunto contiene temperaturas máximas y mínimas de los últimos 365 días para diferentes estaciones meteorológicas del Servicio
# Meteorológico Nacional (SMN). Construya un programa en Python que lee los datos del archivo y los coloca en un diccionario cuyas claves son
# los nombres de las estaciones meteorológicas. El valor asociado a cada clave debe ser otro diccionario con claves "tmax" y "tmin" que mapean con una lista de temperaturas.
#Si no se encuentra registrada una temperatura se la almacenará con el valor None.
#Una  vez cargados los datos se debe hacer un reporte por estación meteorológica de la temperatura máxima y mínima registrada en el período de 1 año.
#Ej.: Si quiero saber la temperatura mínima de Córdoba hace 3 días atrás debo accederla de la siguiente forma
#["CORDOBA OBSERVATORIO"]["tmin"][3]


def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def contar_esp(cadena,lista):
    index = cadena.find(lista[1])
    longitud = len(lista[0])
    return index-longitud

def convertir_fecha(fecha_str):
    return datetime.datetime.strptime(fecha_str, "%d%m%Y").date()

def obtener_temperatura(estacion, tipo, dias_atras):
    fecha_actual = datetime.date.today()
    fecha_deseada = fecha_actual - datetime.timedelta(days=dias_atras)
    if estacion in estaciones and fecha_deseada in estaciones[estacion][tipo]:
        return estaciones[estacion][tipo][fecha_deseada]
    else:
        return "No hay datos para esa fecha"

estaciones= {}
archivo = open("C:/Users/bauti/OneDrive/Desktop/IUA/3er Año/DHS/Registro_temperaturas-02092024/temperaturas.txt","r")
for linea in archivo:
    partes = linea.strip().split()

    fecha_string = partes[0]
    fecha = convertir_fecha(fecha_string)

    if es_numero(partes[1]) and es_numero(partes[2]): #estan las dos temperaturas
        tmax=float(partes[1])
        tmin=float(partes[2])
        nombre=" ".join(partes[3:]) # uso [3:] porque puede tener dos palabras el nombre entonces lo une
    elif not es_numero(partes[1]): #no esta ninguna de las dos temperaturas
        tmax=None
        tmin=None
        nombre=" ".join(partes[1:])
    else: #falta solo una
        if contar_esp(linea,partes)<2:#falta tmin
            tmin=None
            tmax=float(partes[1])
            nombre=" ".join(partes[2:])
        elif contar_esp(linea,partes)>4: #falta tmax
            tmax=None
            tmin=float(partes[1])
            nombre = " ".join(partes[2:])

    if nombre not in estaciones:  # Cuando no esta el nombre de la estacion, lo agrega como CLAVE, y el VALOR es un diccionario que tiene como clave tmax y tmin y los valores son listas
        estaciones[nombre] = {"tmax": {}, "tmin": {}}

    estaciones[nombre]["tmax"][fecha]=tmax
    estaciones[nombre]["tmin"][fecha]=tmin

#ejemplo
dato = obtener_temperatura("ROSARIO AERO", "tmin", 22)
print(dato)
