import argparse
from itertools import product

# Definición del diccionario de leetspeak
leetspeak_dict = {
    'A': ['4', '@', '/-\\'],
    'B': ['8', '|3', '13', '|8', '18'],
    'C': ['<', '(', '{'],
    'D': ['|)', '[)', 'I)', '|>'],
    'E': ['3', '£', '€'],
    'F': ['|=', 'ph', '#'],
    'G': ['6', '9', '&'],
    'H': ['#', '/-/', '[-]', '|-|', '}{'],
    'I': ['1', '!', '|'],
    'J': ['_|', ';', '7'],
    'K': ['|<', '1<', '|{', ']{'],
    'L': ['1', '|_', '£', '|'],
    'M': ['//', '|/|', '^^'],
    'N': ['||', '//', '^/', '/V'],
    'O': ['0', '()', '[]', '{}', '<>'],
    'P': ['|*', '|o', '|>', '|>'],
    'Q': ['9', '0_', '(,)'],
    'R': ['|2', '12', '|?', '|^'],
    'S': ['5', '$', '§'],
    'T': ['7', '+', '-|-', '\'[\''],
    'U': ['|', '_', '||', '/'],
    'V': ['/', '|/', '|'],
    'W': ['//', '^/', '|/'],
    'X': ['%', '><', '}{', ')('],
    'Y': ['`/', '¥', '\'/','|/'],
    'Z': ['2', '>_']
}

def leetspeak_combinations(word):
    """Genera todas las combinaciones posibles de una palabra en leetspeak de manera legible."""
    options = [[char] + leetspeak_dict.get(char.upper(), []) for char in word]
    return [''.join(combination) for combination in product(*options)]

def process_file(input_file, output_file):
    """Lee el archivo de entrada, genera combinaciones y las escribe en el archivo de salida."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip()
            combinations = leetspeak_combinations(word)
            for combo in combinations:
                if combo != word:  # Evita escribir la palabra original
                    outfile.write(combo + '\n')

def main():
    parser = argparse.ArgumentParser(description="Genera combinaciones de leetspeak para contraseñas.")
    parser.add_argument('-l', '--input', required=True, help="Ruta del archivo que contiene las palabras a procesar.")
    parser.add_argument('-o', '--output', required=True, help="Nombre del archivo de salida donde se guardarán las combinaciones.")
    args = parser.parse_args()
    
    process_file(args.input, args.output)

if __name__ == "__main__":
    main()
