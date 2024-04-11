# shwalengthimeter
code for modify string and count original 
def shwalengthimeter(test_strings):
    modified_strings = []  # Inicjalizacja pustej listy, która będzie przechowywać zmodyfikowane stringi
    vowels = set("aeiouy")  # Utworzenie zbioru samogłosek
    for s in test_strings:  # Rozpoczęcie pętli iterującej po każdym stringu w liście test_strings
        modified = "shwa"  # Dodanie "shwa" na początek każdego zmodyfikowanego stringa
        if s[1] in vowels:  # Sprawdzenie, czy drugi znak w oryginalnym stringu jest samogłoską
            modified += s[2:]  # Jeśli tak, dodaj resztę oryginalnego stringa bez drugiego znaku do zmodyfikowanego stringa
        else:
            modified += s[1:]  # Jeśli nie, dodaj resztę oryginalnego stringa bez pierwszego znaku do zmodyfikowanego stringa
        modified += " " + str(len(s))  # Dodanie spacji i długości oryginalnego stringa na koniec zmodyfikowanego stringa
        modified_strings.append(modified)  # Dodanie zmodyfikowanego stringa do listy modified_strings
    return modified_strings  # Zwrócenie listy zmodyfikowanych stringów
Ten kod definiuje funkcję shwalengthimeter, która przyjmuje listę stringów test_strings jako argument i zwraca listę zmodyfikowanych stringów. Pętla for iteruje przez każdy string w test_strings, a następnie dla każdego stringa tworzony jest zmodyfikowany string, który zaczyna się od "shwa". Jeśli drugi znak oryginalnego stringa jest samogłoską, jest on usuwany z zmodyfikowanego stringa. Na koniec długość oryginalnego stringa jest dodawana na końcu zmodyfikowanego stringa, który jest dodawany do listy modified_strings. Funkcja zwraca listę zmodyfikowanych stringów na koniec.
