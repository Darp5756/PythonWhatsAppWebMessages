import json
import os
import pywhatkit
import time

# Cargar números de teléfono
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input', 'telefonos.json'), 'r') as telefonos_json:
        telefonos = json.load(telefonos_json)
except Exception as e:
    print(f"Error al cargar el archivo de teléfonos: {e}")
    exit()

#Cargar mensaje
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input', 'mensaje.txt'), 'r', encoding = 'UTF-8') as mensaje_txt:
        mensaje = mensaje_txt.read()
except Exception as e:
    print(f"Error al cargar el archivo de mensaje: {e}")
    exit()

# Enviar mensajes
errores = 0
for telefono in telefonos:
    try:
        pywhatkit.sendwhatmsg_instantly(telefono, mensaje, tab_close = True)
        print(f"Mensaje enviado a {telefono}")
        time.sleep(5)
    except Exception as e:
        print(f"Se produjo un error con {telefono}: {e}")
        errores += 1

print(f"Se completó el envío de mensajes. Número de errores: {errores}.")
