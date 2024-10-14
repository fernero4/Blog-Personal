import os

def rename_images_in_folder(folder_path):
    # Obtener todos los archivos en la carpeta
    files = os.listdir(folder_path)
    
    # Filtrar solo archivos .png, .jpg y .jpeg
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Ordenar archivos alfabéticamente (opcional)
    image_files.sort()

    # Renombrar los archivos con números secuenciales
    for i, filename in enumerate(image_files, start=1):
        # Obtener la extensión del archivo
        ext = os.path.splitext(filename)[1]
        
        # Crear el nuevo nombre con número secuencial
        new_filename = f"{i}{ext}"
        
        # Ruta completa de los archivos antiguos y nuevos
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Renombrar el archivo
        os.rename(old_file, new_file)

# Ruta a la carpeta que contiene las imágenes
folder_path = 'D:/portfolio/ferh/template/images/tango'
rename_images_in_folder(folder_path)
