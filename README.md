# generador-diplomas-python
Script de Python para generar diplomas masivamente usando la librería Pillow.
# Generador Masivo de Certificados y Diplomas en Python

## Descripción del Proyecto

Este repositorio proporciona una plantilla limpia y funcional para la **generación automatizada de diplomas o certificados** a partir de una plantilla de imagen estática (PNG/JPG) y una lista de datos de alumnos.

El proyecto está diseñado para ser la base de cualquier proceso de creación de documentos personalizados a gran escala, utilizando la potente librería **Pillow** de Python para la manipulación de imágenes.

---

## Requisitos

Asegúrate de que el entorno de ejecución cumpla con los siguientes requisitos:

1.  **Python 3.x**
2.  La librería **Pillow (PIL)**

### Instalación de la Librería

Abre tu terminal y ejecuta el siguiente comando para instalar la dependencia necesaria:

```bash
pip install Pillow

---

Archivo,Función Principal
generador_diplomas_base.py,"Script Principal: Lee la lista de datos y la plantilla, y genera un archivo de imagen (.png) individual por cada registro."
creador_pdf_base.py,Script Secundario: Compila todos los archivos de imagen generados en un único archivo PDF multipágina listo para imprimir o distribuir.

---
Guía de Uso Paso a Paso
Paso 1: Preparación del Entorno
Descarga o clona este repositorio en tu computadora.

Añade tu imagen de plantilla (ej. mi_plantilla.png) en la carpeta del proyecto.

Asegúrate de que la ruta a tu archivo de fuente (.ttf o .otf) sea accesible (ej. C:/Windows/Fonts/times.ttf).

Paso 2: Configurar el Generador (generador_diplomas_base.py)
Abre el archivo generador_diplomas_base.py y modifica la Sección 2: CONFIGURACIÓN INICIAL:

DATOS DE ALUMNOS (Sección 1):

Reemplaza la lista de ejemplo (DATOS_ALUMNOS) con tus datos reales. La estructura debe ser (DNI, Nombre Completo).

Rutas y Nombres:

Actualiza PLANTILLA_DIPLOMA con el nombre exacto de tu imagen de plantilla (ej. 'mi_plantilla.png').

Verifica que la FUENTE_RUTA apunte a una fuente válida en tu sistema.

COORDENADAS (La Parte Crítica):

POS_CENTRO_X: Determina la coordenada horizontal (en píxeles) del punto central donde deseas que se alinee el texto. (El script lo centrará automáticamente respecto a este punto X).

POS_NOMBRE_Y_INICIO: Determina la coordenada vertical (en píxeles) donde debe comenzar el nombre del alumno.

Paso 3: Ejecutar la Generación de Imágenes
Abre la terminal en la carpeta de tu proyecto.

Ejecuta el script principal:

Bash

python generador_diplomas_base.py
El script creará una carpeta llamada diplomas_generados_salida con todos los archivos PNG individuales.

Paso 4: Compilar al Archivo PDF Final
Una vez que todas las imágenes se hayan generado correctamente, ejecuta el script de compilación para unificar los documentos:

Ejecuta el script secundario:

Bash

python creador_pdf_base.py
El script unirá todas las imágenes en un único archivo llamado Documentos_Finales.pdf, listo para su uso.
