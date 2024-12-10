import re

def cargar_indice_invertido(archivo):
    """
    Carga el índice invertido desde el archivo proporcionado.
    Args:
        archivo (str): Ruta del archivo de índice invertido.
    Returns:
        dict: Diccionario con palabras clave y las URL asociadas.
    """
    indice_invertido = {}
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            match = re.match(r'{(.*?):\s*(.*)}', linea.strip())
            if match:
                palabra = match.group(1).strip()
                urls = match.group(2).split()
                indice_invertido[palabra] = set(urls)  # Usamos set para evitar duplicados
    return indice_invertido

def interseccion_listas(listas):
    """
    Calcula la intersección de múltiples conjuntos de URL de forma recursiva.
    Args:
        listas (list): Lista de conjuntos de URL.
    Returns:
        set: Intersección de todas las listas.
    """
    if len(listas) == 0:
        return set()
    if len(listas) == 1:
        return listas[0]
    return listas[0].intersection(interseccion_listas(listas[1:]))

def buscar_consulta(consulta, indice_invertido):
    """
    Realiza una búsqueda en el índice invertido.
    Args:
        consulta (str): Consulta ingresada por el usuario.
        indice_invertido (dict): Índice invertido.
    Returns:
        set: Conjunto de URL donde se encuentran todos los términos de la consulta.
    """
    palabras = consulta.split()
    listas_urls = [indice_invertido.get(palabra, set()) for palabra in palabras]
    resultado = interseccion_listas(listas_urls)
    return resultado

def main():
    archivo = 'lista_invertida_limpia.txt'
    resultados_archivo = 'resultados_busqueda.txt'

    print(f'Cargando índice invertido desde el archivo "{archivo}"...')
    indice_invertido = cargar_indice_invertido(archivo)
    print(f'Índice invertido cargado correctamente con {len(indice_invertido)} términos.\n')

    with open(resultados_archivo, 'w', encoding='utf-8') as salida:
        while True:
            consulta = input("Ingrese su consulta (o escriba 'salir' para terminar): ").strip().lower()
            if consulta == 'salir':
                print("Saliendo del buscador...")
                break
            if not consulta:
                print("La consulta no puede estar vacía. Inténtelo de nuevo.\n")
                continue

            resultado = buscar_consulta(consulta, indice_invertido)
            if resultado:
                print(f'Resultados encontrados ({len(resultado)}):')
                salida.write(f'Consulta: {consulta}\n')
                salida.write(f'Resultados encontrados ({len(resultado)}):\n')
                for url in resultado:
                    print(f' - {url}')
                    salida.write(f' - {url}\n')
                salida.write('\n')
            else:
                print("No se encontraron resultados para la consulta.\n")
                salida.write(f'Consulta: {consulta}\n')
                salida.write("No se encontraron resultados.\n\n")

    print(f"Resultados almacenados en '{resultados_archivo}'.")

if __name__ == "__main__":
    main()
