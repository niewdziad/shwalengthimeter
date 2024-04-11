def shwalengthimeter(test_strings):
    modified_strings = []  # Inicjalizacja pustej listy, która będzie przechowywać zmodyfikowane stringi
    vowels = set("aeiouy")  # Utworzenie zbioru samogłosek
    for s in test_strings:  # Rozpoczęcie pętli iterującej po każdym stringu w liście test_strings
        modified = "shwa"  # Dodanie "shwa" na początek każdego zmodyfikowanego stringa
        if s[1] in vowels:  # Sprawdzenie, czy drugi znak w oryginalnym stringu jest samogłoską
            modified += s[2:]  # Jeśli tak, dodaj resztę oryginalnego stringa od trzeciego znaku do zmodyfikowanego stringa
        else:
            modified += s[1:]  # Jeśli nie, dodaj resztę oryginalnego stringa bez pierwszego znaku do zmodyfikowanego stringa
        modified += " " + str(len(s))  # Dodanie spacji i długości oryginalnego stringa na koniec zmodyfikowanego stringa
        modified_strings.append(modified)  # Dodanie zmodyfikowanego stringa do listy modified_strings
    return modified_strings  # Zwrócenie listy zmodyfikowanych stringów

# input
test_strings = ["kawabunga", "metro2013", "moon", "orange"]

# output
print(shwalengthimeter(test_strings))