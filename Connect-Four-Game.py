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

wyswietlaniePlanszy(plansza)