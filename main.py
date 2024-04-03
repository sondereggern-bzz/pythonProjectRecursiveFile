import os

def file_names_to_csv(folder_path, output_file, file_extension=None):
    try:
        file_names = []
        file_paths = []
        file_sizes = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file_extension is None or file.endswith(file_extension):
                    file_paths.append(os.path.join(root, file))
                    file_names.append(file)
                    file_sizes.append(os.path.getsize(os.path.join(root, file)))

        file_data = list(zip(file_names, file_paths, file_sizes))
        file_data.sort()

        with open(output_file, 'w') as csv_file:
            for file_name, file_path, file_size in file_data:
                csv_file.write(f"{file_name}; {file_path}; {file_size} bytes\n")

        print(f"Die Dateinamen wurden Erfolgreich in '{output_file}' geschrieben.")
    except Exception as e:
        print(f"Fehler beim Schreiben der Dateinamen: {e}")

# Beispielaufruf
folder_path = r'C:\Users\nicso\Documents'
output_file = r'C:\Users\nicso\PycharmProjects\pythonProjectRecursiveFile\dateinamen.csv'

file_extension = input("Geben Sie die Dateiendung ein (ohne Punkt) oder Enter um nicht zu filtern: ").strip()
if file_extension:
    file_extension = "." + file_extension

file_names_to_csv(folder_path, output_file, file_extension)
