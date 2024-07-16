import os

def listar_archivos(directorio):
    try:
        # Recorre el directorio
        for root, dirs, files in os.walk(directorio):
            # Imprime cada archivo encontrado
            for file in files:
                print(os.path.join(root, file))
    except Exception as e:
        print(f"Error: {e}")

# Directorio que quieres recorrer (puedes cambiarlo según tus necesidades)
directorio = "F:\GitHub\Tarot_IA\BD-tarot\Barajas\Estandar (ES)"

# Llamada a la función
listar_archivos(directorio)
