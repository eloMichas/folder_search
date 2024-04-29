
    #Program ma za zadanie znalezienie frazy w folderze
    #w którym jest więcej plików niż jedno


#import OS i RE
import os
import re

#Funkcja przeszukująca kilka plików .txt w celu znalezienia frazy
def search_in_files(catalog, phrase):
    for txt_file in os.listdir(catalog):
        if txt_file.endswith('.txt'):
            with open(os.path.join(catalog, txt_file), 'r') as file:
                contents = file.read()
                if re.search(phrase, contents, re.IGNORECASE):
                    print(f"Znaleziono dopasowanie w pliku: {txt_file}")

#Lokalizacja katalogu do przeszukania
catalog = 'C://Users//mlawn//Desktop//test'

#Pytanie jakiej frazy wyszukać
what_to_search = input("Jakiego słowa szukasz?: ")
phrase = rf"{what_to_search}"

search_in_files(catalog, phrase)
