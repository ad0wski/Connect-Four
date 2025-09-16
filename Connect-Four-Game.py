plansza = [[" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "]]

aktualnyGracz = "X"

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

