# Python WhatsApp Web Messages

Script de Python para enviar mensajes automáticos mediante WhatsApp Web.

## Instalación

Python debe estar instalado.

Todos los comandos se ejecutan en la raíz del proyecto.

1. Crea el entorno virtual (venv para que aplique el `.gitignore`).
```bash
python -m venv venv
```

2. Activa el entorno virtual.
###### Windows
```bash
.\venv\Scripts\activate
```
###### Linux y MacOS
```bash
source ./venv/Scripts/activate
```

3. Instala las dependencias.
```bash
pip install -r requirements.txt
```

4. Copia los archivos de funcionamiento a la carpeta input.
###### Windows
```bash
copy templates\* input
```
###### Linux y MacOS
```bash
cp templates/* input
```

## Configuración

1. Coloca el mensaje que quieres enviar en el archivo `mensajes.txt`.

2. Coloca en el archivo `telefonos.json` los números de teléfono que recibirán el mensaje.

3. Asegurate de haber iniciado sesión en WhatsApp Web, acceder para que se carguen todos los mensajes y luego cerrar la pestaña para evitar duplicidad de la misma.

## Ejecución

1. Ejecuta el programa.
```bash
python src/main.py
```

2. Uno por uno, se abrirá la pestaña en el navegador, se abrirá el chat con el número de teléfono correspondiente, se colocará el mensaje, se enviará y la pestaña se cerrará.

3. Para finalizar el servidor virtual una vez terminado de ejecutar el programa las veces que sea necesario.
```bash
deactivate
```