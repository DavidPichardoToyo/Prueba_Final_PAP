from clases import *
import datetime
import pytz

tz_CL = pytz.timezone("America/Santiago")
datetime_CL = datetime.datetime.now(tz_CL)

un_mes = datetime_CL + datetime.timedelta(days=30)
hoy = datetime_CL.strftime("%d/%m/%Y")

cam = Campana("Prueba", hoy, un_mes.strftime("%d/%m/%Y"))

try:
    nuevo_nombre_campana = input("Ingrese el nuevo nombre de la campaña: ")
    cam.nombre = nuevo_nombre_campana

    print("Los subtipos soportados para el siguiente formato son:")
    Video.mostrar_formatos()
    nuevo_sub_tipo = input("\nIngrese el nuevo subtipo: ")

    cam.anuncios[0].sub_tipo = nuevo_sub_tipo
except Exception as e:
    with open("error.log", "a+") as log:
        log.write(f"{datetime_CL.strftime('%d/%m/%Y %H:%M:%S')}, {e} \n")

