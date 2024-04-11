# shwalengthimeter
code for modify string and count original 
def shwalengthimeter(test_strings): - Ta linia definiuje funkcję shwalengthimeter, która przyjmuje listę stringów test_strings jako argument.

modified_strings = [] - Tworzy pustą listę modified_strings, która będzie przechowywać zmodyfikowane stringi.

vowels = set("aeiouy") - Tworzy zbiór samogłosek ("aeiouy"). Używamy zbioru, ponieważ jest to bardziej efektywne niż lista do sprawdzania obecności elementów.

for s in test_strings: - Rozpoczyna pętlę for, która iteruje przez każdy string w liście test_strings.

modified = "shwa" + s[1:] - Tworzy zmienną modified, która jest złożeniem słowa "shwa" i fragmentu stringu s od drugiego znaku do końca.

if s[1] in vowels: - Sprawdza, czy drugi znak stringu s jest samogłoską.

modified = modified[0] + modified[2:] - Jeśli drugi znak jest samogłoską, usuwa go z modified, pozostawiając tylko pierwszy znak i fragment od trzeciego znaku do końca.

modified += " " + str(len(s)) - Do modified dodaje spację, a następnie długość oryginalnego stringu s przekonwertowaną na string.

modified_strings.append(modified) - Dodaje zmodyfikowany string modified do listy modified_strings.

return modified_strings - Zwraca listę modified_strings zawierającą zmodyfikowane stringi.

Po zdefiniowaniu funkcji, przykładowe dane wejściowe są podane jako test_strings. Funkcja shwalengthimeter jest wywoływana z tymi danymi wejściowymi, a wynik jest wyświetlany za pomocą funkcji print.
