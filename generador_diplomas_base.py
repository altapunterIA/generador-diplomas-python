from PIL import Image, ImageDraw, ImageFont
import os
import sys

# =========================================================================
# === 1. DATOS DE EJEMPLO (¡MODIFICAR AQUÍ!) ===============================
# =========================================================================
# Estructura: (DNI, Nombre Completo)
# Aquí se deben listar todos los alumnos que recibirán el diploma.
DATOS_ALUMNOS = [
    ("12345678", "ALUMNO EJEMPLO UNO"),
    ("98765432", "ALUMNA PRUEBA DOS"),
    ("11223344", "NOMBRE TRES, APELLIDO LARGO"),
    ("44556677", "CUARTO ALUMNO DE PRUEBA"),
]


# =========================================================================
# === 2. CONFIGURACIÓN INICIAL (¡AJUSTAR ANTES DE EJECUTAR!) ==============
# =========================================================================

# ARCHIVOS CLAVE
# 1. Nombre de tu plantilla de diploma. DEBE estar en la misma carpeta que este script.
PLANTILLA_DIPLOMA = 'tu_plantilla.png'  
# 2. Carpeta donde se guardarán los diplomas generados.
CARPETA_SALIDA = 'diplomas_generados_salida'

# RUTA DE FUENTE: Usa una fuente TTF/OTF de tu sistema (Windows, Mac o Linux)
# Si estás en Windows, prueba: 'C:/Windows/Fonts/times.ttf'
FUENTE_RUTA = 'C:/Windows/Fonts/times.ttf' 

# TAMAÑOS DE FUENTE
TALLA_NOMBRE = 70
TALLA_DNI = 50

# COORDENADAS (VALORES INICIALES - AJUSTAR PARA TU PLANTILLA)
# Estos valores son CRUCIALES. Debes abrír tu plantilla en un editor 
# de imágenes para determinar el centro (X) y las alturas (Y).
POS_CENTRO_X = 1200          
# Altura vertical (Y) donde empieza el nombre.
POS_NOMBRE_Y_INICIO = 450    

# Color del texto (RGB: 0, 0, 0 es Negro)
COLOR_TEXTO = (0, 0, 0) 


# =========================================================================
# === 3. FUNCIÓN PRINCIPAL (Generación del Diploma) =======================
# =========================================================================

def generar_diploma(dni, nombre_completo):
    """Genera un diploma individual con el DNI y nombre proporcionados."""
    try:
        # Cargar la imagen y la fuente
        img = Image.open(PLANTILLA_DIPLOMA).convert("RGB")
        draw = ImageDraw.Draw(img)
        font_nombre = ImageFont.truetype(FUENTE_RUTA, TALLA_NOMBRE)
        font_dni = ImageFont.truetype(FUENTE_RUTA, TALLA_DNI)
        
    except FileNotFoundError as e:
        print(f"Error fatal: No se encontró un archivo clave: {e}")
        print("Revisa la variable PLANTILLA_DIPLOMA y/o FUENTE_RUTA en la Sección 2.")
        sys.exit(1) # Detiene la ejecución si hay error crítico
    
    # Prepara el texto
    texto_nombre = nombre_completo.upper()
    texto_dni = f"DNI: {dni}"
    
    # 1. Centrado del Nombre
    bbox_nombre = draw.textbbox((0, 0), texto_nombre, font=font_nombre)
    ancho_nombre = bbox_nombre[2] - bbox_nombre[0]
    alto_nombre = bbox_nombre[3] - bbox_nombre[1]

    # Calcula la posición X para que el texto quede centrado
    x_nombre = POS_CENTRO_X - (ancho_nombre / 2)
    y_nombre = POS_NOMBRE_Y_INICIO
    draw.text((x_nombre, y_nombre), texto_nombre, fill=COLOR_TEXTO, font=font_nombre)

    # 2. Centrado del DNI (Debajo del nombre)
    bbox_dni = draw.textbbox((0, 0), texto_dni, font=font_dni)
    ancho_dni = bbox_dni[2] - bbox_dni[0]
    
    x_dni = POS_CENTRO_X - (ancho_dni / 2)
    # Coloca el DNI 10 píxeles debajo del nombre
    y_dni = y_nombre + alto_nombre + 10 
    draw.text((x_dni, y_dni), texto_dni, fill=COLOR_TEXTO, font=font_dni)

    # Guarda la imagen
    nombre_archivo_salida = os.path.join(CARPETA_SALIDA, f"Diploma_{nombre_completo.replace(' ', '_').replace('.', '')}.png")
    img.save(nombre_archivo_salida)
    print(f"Generado: {nombre_archivo_salida}")


# =========================================================================
# === 4. PROGRAMA PRINCIPAL (EJECUCIÓN) ===================================
# =========================================================================

if __name__ == "__main__":
    
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)
    
    print(f"Iniciando la generación de {len(DATOS_ALUMNOS)} diplomas en: {CARPETA_SALIDA}")
    
    # Itera sobre la lista de DNI y Nombre
    for dni, nombre_completo in DATOS_ALUMNOS:
        generar_diploma(dni, nombre_completo)
        
    print("\nProceso de generación finalizado.")