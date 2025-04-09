"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_OUTPUT_FILE = "sorted_words.txt"


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


def save_to_file(items, filename):
    """Guarda la lista de palabras ordenadas en un archivo."""
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
    print(f"Se ha guardado el resultado en {filename}")


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    output_filename = DEFAULT_OUTPUT_FILE
    
    # Procesamiento de argumentos
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    elif len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        output_filename = sys.argv[3]
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento es el archivo de salida (opcional)")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Ordenar la lista de palabras
    sorted_words = sort_list(word_list)

    # Guardar el resultado en un archivo
    save_to_file(sorted_words, output_filename)

