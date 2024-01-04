import os
import inspect
from cryptography.fernet import Fernet ,InvalidToken

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
                files.append(file_path)

    
    return files

def decr(files):
    # Leggi la chiave segreta dal file thekey.key
    with open("thekey.key", "rb") as key_file:
        secret_key = key_file.read()

    user_phrase = input("Inserisci la parola segreta\n")

    if user_phrase == "king":
        for f in files:
            with open(f, "rb") as file:
                contents = file.read()

            try:
                cipher = Fernet(secret_key)
                contents_decrypted = cipher.decrypt(contents)

                with open(f, "wb") as file:
                    file.write(contents_decrypted)

                print(f"File {f} decifrato con successo.")
            except InvalidToken:
                print(f"Errore durante la decifratura del file {f}. Chiave segreta non corretta o dati danneggiati.")
    else:
        print("Parola errata!")
        
def get_parent_directory(path):
    return os.path.dirname(path)

parent_dir= get_parent_directory(os.getcwd())
files = search(parent_dir)
decr(files)




