# Buscador Basado en Índice Invertido

Este proyecto implementa un sencillo buscador utilizando un **índice invertido**. Un índice invertido asocia cada palabra clave con las URLs en las que aparece, lo que permite encontrar rápidamente todas las URLs que contienen un determinado conjunto de palabras.

## Características

- **Carga de Índice Invertido:**  
  Lee un archivo de texto que contiene el índice invertido en un formato específico.
  
- **Búsqueda Eficiente:**  
  Realiza búsquedas de consultas compuestas por una o varias palabras, devolviendo las URLs que contienen **todas** las palabras de la consulta.
  
- **Interfaz de Consola:**  
  Permite al usuario ingresar consultas de manera interactiva y muestra los resultados en la consola.
  
- **Evita Duplicados:**  
  Utiliza conjuntos (`set`) para almacenar URLs, asegurando que no haya duplicados en los resultados.

## Estructura del Proyecto

- **buscador.py**: Script principal en Python que implementa las funcionalidades del buscador.
- **lista_invertida_limpia.txt**: Archivo de texto que contiene el índice invertido en el formato requerido.

## ¿Cómo funciona?

1. **Carga del Índice Invertido:**  
   El script lee el archivo `lista_invertida_limpia.txt`, donde cada línea sigue la estructura:

Durante la carga:
- Se utilizan expresiones regulares para extraer la palabra y las URLs asociadas.
- Las URLs se almacenan en conjuntos (`set`) para evitar duplicados.

2. **Búsqueda:**  
Al recibir una consulta, el buscador:
- Separa la consulta en palabras.
- Obtiene el conjunto de URLs asociado a cada palabra.
- Calcula la intersección de todos estos conjuntos, resultando en las URLs que contienen **todas** las palabras de la consulta.

3. **Interfaz por Consola:**  
El programa solicita al usuario una consulta y muestra las URLs resultantes.
- Si se teclea `"salir"`, el buscador termina.
- Si la consulta está vacía, pide ingresar algo válido.
- Si no hay coincidencias, informa que no se encontraron resultados.

## Ejecución

### Requisitos Previos

- **Python 3** instalado en tu sistema.

### Pasos para Ejecutar

1. **Preparar el Archivo de Índice Invertido:**
- Crea un archivo de texto llamado `lista_invertida_limpia.txt` en el mismo directorio que el script `buscador.py`.
- Cada línea del archivo debe seguir el formato:
  ```
  {palabra: url1 url2 url3 ...}
  ```
  Por ejemplo:
  ```
  {python: https://www.python.org https://docs.python.org}
  {documentación: https://docs.python.org}
  {buscador: https://ejemplo.com/buscador}
  ```

2. **Ejecutar el Script:**
Abre una terminal, navega al directorio que contiene `buscador.py` y ejecuta:
```bash
python3 script_busqueda.py
