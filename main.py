import os
import random
import string


def cancella_righe(estensioni=None, perc_lines=5, perc_chars=5, directory=None):
    # Verifico che la directory sia specificata
    if directory is None or not os.path.exists(directory):
        raise ValueError("Devi specificre una directory, oppure la directory specificata non esiste.")

    # Verifico che l'estensione/i vengano specificate
    # Se si vuole prendere tutti i file(tutte le estensioni), basta commentare questa parte del codice
    if estensioni is None:
        raise ValueError("L'estensione/i non è/sono stata/e specificata/e")

    # Scansiono ricorsivamente la directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Verifico che il file abbia una delle l'estensioni specificate
            # Se non viene specificato l'estensione prendo tutti i file
            if not estensioni or file.endswith(tuple(estensioni)):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                num_lines = len(lines)

                # Calcolo le righe da eliminare
                num_lines_to_delete = max(int(num_lines * perc_lines / 100), 1)
                # Seleziono casualmente le righe da eliminare
                lines_to_delete = random.sample(range(num_lines), num_lines_to_delete)

                # Modifico le linee
                modified_lines = []
                for i, line in enumerate(lines):
                    # Se la linea non deve essere eliminata
                    if i not in lines_to_delete:
                        # calcolo il numero di caratteri da modificare
                        num_chars_to_modify = max(int(len(line) * perc_chars / 100), 1)
                        chars_to_modify = random.sample(range(len(line)), num_chars_to_modify)
                        modified_line = ''.join(
                            char if char_index not in chars_to_modify else random.choice(
                                string.ascii_letters + string.digits)
                            for char_index, char in enumerate(line)
                        )
                        # Aggiungo la linea modificata alla lista
                        modified_lines.append(modified_line)
                # Sovrascrivo il file originale con le linee modificate
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("".join(modified_lines))


if __name__ == "__main__":
    try:
        cancella_righe(estensioni=[".txt"], perc_lines=4, perc_chars=6, directory="C:/Users/Tanveer/Desktop/Engim")
    except ValueError as e:
        print(e)
