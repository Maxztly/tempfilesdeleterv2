import os
import shutil
import customtkinter as ctk

def delete_temp_files(temp_directory):
    for file in os.listdir(temp_directory):
        file_path = os.path.join(temp_directory, file)
        file_path = os.path.realpath(file_path)  # Get the real path of the file

        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Erfolgreich gelöscht: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Erfolgreich gelöscht: {file_path}")
        except Exception as e:
            print(f"Fehler beim Löschen von {file_path}: {str(e)}")

def create_gui():
    root = ctk.CTk()

    # Setze den Titel
    root.title("TEMP FILES DELETER")

    # Setze das Icon
    root.iconbitmap('trash.ico.ico')

    # Fenstergröße
    window_width = 300
    window_height = 100

    # Bildschirmauflösung
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Berechne die Position für das Fenster
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Setze die Position des Fensters
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Konfiguriere das Grid-Layout
    root.grid_rowconfigure(0, weight=2)  # 40% Rand oben
    root.grid_rowconfigure(1, weight=3)  # 60% Button
    root.grid_rowconfigure(2, weight=2)  # 40% Rand unten
    root.grid_columnconfigure(0, weight=2)  # 40% Rand links
    root.grid_columnconfigure(1, weight=3)  # 60% Button
    root.grid_columnconfigure(2, weight=2)  # 40% Rand rechts

    # Lösche Dateien in beiden Verzeichnissen, wenn der Button gedrückt wird
    def delete_files():
        delete_temp_files(os.environ.get('TEMP'))
        delete_temp_files('C:\\Windows\\Temp')

    button = ctk.CTkButton(root, text="Delete Tempfiles", command=delete_files)
    button.grid(row=1, column=1, sticky="nsew")  # Positioniere den Button in der Mitte und lasse ihn sich dynamisch anpassen

    root.mainloop()


if __name__ == "__main__":
    create_gui()