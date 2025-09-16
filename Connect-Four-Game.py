plansza = [[" ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " "]]

zasady = """
Zasady gry: Connect Four 🎮

1. Gra odbywa się na planszy 7 kolumn x 6 wierszy.
2. Gracze na zmianę wrzucają swoje pionki: X lub 0.
3. Aby wykonać ruch, wybierz numer kolumny (1–7).
4. Pionek zawsze spada na najniższe wolne miejsce w danej kolumnie.
5. Wygrywa gracz, który jako pierwszy ułoży 4 swoje symbole w rzędzie:
   poziomo, pionowo lub po skosie.
6. Jeśli cała plansza się zapełni i nikt nie wygrał — jest remis.
"""
print(zasady)

def zmianaGracza(aktualnyGracz):
    if aktualnyGracz == "X":
        aktualnyGracz = "0"
    else:
        aktualnyGracz = "X"
    return aktualnyGracz

def wyswietlaniePlanszy(plansza):
        print("\n")
        for i in range(6):
            for j in range(7):
                if j == 0:
                     print(f"|{plansza[i][j]}", end=" |")
                else:
                     print(f"{plansza[i][j]}", end=" |")
            print()
        print("======================")
        print(" 1  2  3  4  5  6  7")

def ruchGracza(aktualnyGracz, plansza):
    czyPoprawnieWstawionePole = False
    while czyPoprawnieWstawionePole == False:
        czyZajeteWszystkieMiejsca = True
        wyborKolumny = int(input("Wybierz kolumnę: "))
        kolumna = wyborKolumny - 1 #dajemy to jako index do planszy
        if wyborKolumny > 0 and wyborKolumny < 8:
            for i in range(5, -1, -1):
                if plansza[i][kolumna] == " ":
                    plansza[i][kolumna] = aktualnyGracz
                    czyZajeteWszystkieMiejsca = False
                    czyPoprawnieWstawionePole = True
                    break
            if czyZajeteWszystkieMiejsca == True:
                print("Ta kolumna jest pełna! ")
        else:
            print("Wybierz kolumnę w zakresie 1 - 7")

def czyWygrana(plansza, aktualnyGracz):
    for i in range(6):
        for j in range(4):
            if (plansza[i][j] == aktualnyGracz and
                plansza[i][j+1] == aktualnyGracz and
                plansza[i][j+2] == aktualnyGracz and
                plansza[i][j+3] == aktualnyGracz):
                return True
    for i in range(3):
        for j in range(7):
            if (plansza[i][j] == aktualnyGracz and
                plansza[i+1][j] == aktualnyGracz and
                plansza[i+2][j] == aktualnyGracz and
                plansza[i+3][j] == aktualnyGracz):
                return True
    for i in range(3):
        for j in range(4):
            if (plansza[i][j] == aktualnyGracz and
                plansza[i+1][j+1] == aktualnyGracz and
                plansza[i+2][j+2] == aktualnyGracz and
                plansza[i+3][j+3] == aktualnyGracz):
                return True
    for i in range(3, 6):
        for j in range(4):
            if (plansza[i][j] == aktualnyGracz and
                plansza[i-1][j+1] == aktualnyGracz and
                plansza[i-2][j+2] == aktualnyGracz and
                plansza[i-3][j+3] == aktualnyGracz):
                return True
    return False

ruchy = 0
aktualnyGracz = "X"

while True:
    ruchy += 1

    wyswietlaniePlanszy(plansza)
    ruchGracza(aktualnyGracz, plansza)

    if czyWygrana(plansza, aktualnyGracz) == True:
        wyswietlaniePlanszy(plansza)
        print(f"\nWYGRYWA {aktualnyGracz}! \n")
        break

    if ruchy == 42:
        wyswietlaniePlanszy(plansza)
        print(f"\nREMIS! \n")
        break
    
    aktualnyGracz = zmianaGracza(aktualnyGracz)