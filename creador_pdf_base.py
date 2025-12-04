from PIL import Image
import os
import sys

# =========================================================================
# === 1. CONFIGURACIÓN DE PDF (DEBE COINCIDIR CON EL GENERADOR) ===========
# =========================================================================
CARPETA_IMAGENES = 'diplomas_generados_salida' # Carpeta de salida del script generador
NOMBRE_PDF_SALIDA = 'Documentos_Finales.pdf'
FORMATOS_PERMITIDOS = ('.png', '.jpg', '.jpeg') 

# =========================================================================
# === 2. FUNCIÓN DE CREACIÓN DE PDF (NO MODIFICAR) ========================
# =========================================================================

def crear_pdf_de_imagenes():
    """Busca todas las imágenes en la carpeta de salida y las une en un único PDF."""
    
    if not os.path.exists(CARPETA_IMAGENES):
        print(f"Error: La carpeta '{CARPETA_IMAGENES}' no existe. Ejecuta primero el generador de diplomas.")
        sys.exit(1)

    rutas_imagenes = []
    for nombre_archivo in os.listdir(CARPETA_IMAGENES):
        if nombre_archivo.lower().endswith(FORMATOS_PERMITIDOS):
            rutas_imagenes.append(os.path.join(CARPETA_IMAGENES, nombre_archivo))
            
    if not rutas_imagenes:
        print(f"Advertencia: No se encontraron imágenes en la carpeta '{CARPETA_IMAGENES}'.")
        return

    rutas_imagenes.sort()

    try:
        primera_imagen = Image.open(rutas_imagenes[0]).convert('RGB')
        
    except Exception as e:
        print(f"Error al abrir la primera imagen '{rutas_imagenes[0]}': {e}")
        return

    lista_de_paginas = []
    for ruta in rutas_imagenes[1:]:
        try:
            img = Image.open(ruta).convert('RGB')
            lista_de_paginas.append(img)
        except:
            pass # Ignora archivos corruptos
            
    try:
        primera_imagen.save(
            NOMBRE_PDF_SALIDA,
            "PDF", 
            resolution=100.0, 
            save_all=True, 
            append_images=lista_de_paginas
        )
        print(f"\nPDF Creado con Éxito: '{NOMBRE_PDF_SALIDA}'")
        
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")

# =========================================================================
# === 3. PROGRAMA PRINCIPAL (EJECUCIÓN) ===================================
# =========================================================================

if __name__ == "__main__":
    crear_pdf_de_imagenes()