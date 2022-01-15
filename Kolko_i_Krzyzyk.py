
#tworzenie zmiennych
tablica = [ [None] * 3, [None] * 3, [None] * 3 ]
czyja_tura = 'X'
kto_wygral = None
remis = False
def WyswietlPlansze():
    print("Plansza")
    print("  123")
    for y in range(3):
        print(format(y+1) + " ",end='')
        for komorka in tablica[y]:
            if komorka == None:
                print('_',end='')
            else:
                print(komorka,end='')
        print('')


while remis == False and kto_wygral is None:
    WyswietlPlansze()
    print("ruch gracza", czyja_tura)
    x = int(input("podaj wspolrzedna X (miedzy 1 i 3):"))
    y = int(input("podaj wspolrzedna Y (miedzy 1 i 3):"))

    if tablica[y - 1][x - 1] is None:
        tablica[y - 1][x - 1] = czyja_tura # ustawiamy pionek na planszy

        # sprawdzamy czy wygral ktorys gracz
        for wiersz in tablica: # sprawdzamy wiersze
            if wiersz[0] is not None and wiersz[1] is not None and wiersz[2] is not None :
                if wiersz[0] == wiersz[1] == wiersz[2]:
                    kto_wygral = czyja_tura
        for k in range(3): # sprawdzamy kolumny
            if tablica[k][0] is not None and tablica[k][1] is not None and tablica[k][2] is not None :
                if tablica[k][0] == tablica[k][1] == tablica[k][2]:
                    kto_wygral = czyja_tura
        # sprawdzamy przekatne 1
        if tablica[0][0] is not None and tablica[1][1] is not None and tablica[2][2] is not None :
            if tablica[0][0] == tablica[1][1] == tablica[2][2]:
                kto_wygral = czyja_tura
        # sprawdzamy przekatne 2
        if tablica[0][2] is not None and tablica[1][1] is not None and tablica[2][0] is not None:
            if tablica[0][2] == tablica[1][1] == tablica[2][0]:
                kto_wygral = czyja_tura
        # sprawdzamy czy remis
        if kto_wygral is None:
            brakpustych = True
            for wiersz in tablica:
                for komorka in wiersz:
                    brakpustych &= komorka is not None
            remis = brakpustych
        # jesli zaden nie wygral ani nie remis to zmieniamy gracza
        if kto_wygral is None and remis == False:
            if czyja_tura == "X":  # zmiana gracza
                czyja_tura = "O"
            else:
                czyja_tura = "X"
    else:
        print("to pole jest zajete")

WyswietlPlansze()
if remis:
    print("Remis")
else:
    print("Wygral gracz", czyja_tura)



