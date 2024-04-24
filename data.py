favMovies = [
    {
        "title": "Harry Potter i Zakon Feniksa",
        "year": 2007,
        "rating": 7.5,
        "description": "Piąta część serii filmowej opartej na książkach J.K. Rowling, gdzie Harry Potter i jego przyjaciele zakładają tajny zakon, aby stawić czoła rosnącemu zagrożeniu ze strony Czarnego Pana, Lorda Voldemorta.",
        "reżyserzy": ["David Yates"],
        "scenarzyści": ["Michael Goldenberg"],
        "gwiazdy": ["Daniel Radcliffe", "Emma Watson", "Rupert Grint"],
        "gatunki": ["Fantasy", "Przygodowy"]
    },
    {
        "title": "Władca Pierścieni: Powrót Króla",
        "year": 2003,
        "rating": 8.9,
        "description": "Trzecia część epickiej trylogii fantasy opartej na książkach J.R.R. Tolkiena, gdzie Aragorn prowadzi sojusz ludzi w ostatecznej bitwie o Przesmyk Czarnego Pana, Saurona.",
        "reżyserzy": ["Peter Jackson"],
        "scenarzyści": ["Fran Walsh", "Philippa Boyens", "Peter Jackson"],
        "gwiazdy": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
        "gatunki": ["Fantasy", "Przygodowy", "Dramat"]
    },
    {
        "title": "Forrest Gump",
        "year": 1994,
        "rating": 8.8,
        "description": "Historia życia Forresta Gumpa, mężczyzny o niskim ilorazie inteligencji, który przypadkowo staje się świadkiem i uczestnikiem wielu kluczowych wydarzeń w historii Stanów Zjednoczonych.",
        "reżyserzy": ["Robert Zemeckis"],
        "scenarzyści": ["Eric Roth"],
        "gwiazdy": ["Tom Hanks", "Robin Wright", "Gary Sinise"],
        "gatunki": ["Dramat", "Romans", "Komedia"]
    },
    {
        "title": "Znachor",
        "year": 1982,
        "rating": 7.8,
        "description": "Film oparty na życiu Eugeniusza Makulskiego, lekarza, który w okresie międzywojennym próbował wprowadzić nowoczesne metody leczenia na polskiej prowincji.",
        "reżyserzy": ["Jerzy Hoffman"],
        "scenarzyści": ["Włodzimierz Odojewski", "Tadeusz Konwicki"],
        "gwiazdy": ["Wojciech Wysocki", "Teresa Sawicka", "Leszek Teleszyński"],
        "gatunki": ["Dramat", "Biograficzny"]
    }
]

# Wyświetlanie danych z dodatkowymi ciągami przed polami
if __name__ == "__main__":
    # 'Tytuł' pierwszego filmu
    print(f"Tytuł pierwszego filmu to: '{favMovies[0]['title']}'")

    # 'Rok' drugiego filmu
    print(f"Rok premiery drugiego filmu to: {favMovies[1]['year']}")

    # 'Ocena' trzeciego filmu
    print(f"Ocena IMDB trzeciego filmu to: {favMovies[2]['rating']}")

    # 'Opis' czwartego filmu
    print(f"Krótki opis czwartego filmu to: '{favMovies[3]['description']}'")

#Przedstawienie nowych informacji
    
    # Pierwszy reżyser pierwszego filmu
    first_director = favMovies[0]["reżyserzy"][0]
    print(f"Głównym reżyserem pierwszego filmu jest: '{first_director}'")

    # Pierwszy scenarzysta drugiego filmu
    first_writer = favMovies[1]["scenarzyści"][0]
    print(f"Głównym scenarzystą drugiego filmu jest: '{first_writer}'")

    # Pierwsza gwiazda trzeciego filmu
    first_star = favMovies[2]["gwiazdy"][0]
    print(f"Główną gwiazdą trzeciego filmu jest: '{first_star}'")

    # Pierwszy gatunek czwartego filmu
    first_genre = favMovies[3]["gatunki"][0]
    print(f"Głównym gatunkiem czwartego filmu jest: '{first_genre}'")

 # Obliczanie średniej oceny filmów
ratings = [movie["rating"] for movie in favMovies]  # Lista ocen filmów
averageRating = sum(ratings) / len(ratings)  # Obliczenie średniej oceny

# Przypisanie średniej oceny do zmiennej averageRating
if __name__ == "__main__":
    print(f"Średnia ocena filmów: {averageRating}")

# Obliczanie średniego wieku filmów
current_year = 2024  # Zakładamy bieżący rok jako 2024

# Oblicz wiek każdego filmu na podstawie roku premiery
ages = [current_year - movie["year"] for movie in favMovies]

# Oblicz średni wiek filmów
averageAge = sum(ages) / len(ages)

# Przypisanie średniego wieku do zmiennej averageAge
if __name__ == "__main__":
    print(f"Średni wiek filmów: {averageAge} lat")