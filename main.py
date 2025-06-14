"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Natálie Zýková
email: natalie.zykova@seznam.cz
"""

# vytvoření tajného čísla

import random as rd
import time

prvni_cifra = rd.randint(1,9)
prvni_cifra_str = str(prvni_cifra)

seznam_cifry = []
seznam_cifry.append(prvni_cifra_str)

moznosti = list(range(0,10))
moznosti.remove(prvni_cifra)

cifry = rd.sample(moznosti, 3)

for cifra in cifry:
    cifra_str = str(cifra)
    seznam_cifry.append(cifra_str)

tajne = "".join(seznam_cifry)
tajne_str = str(tajne)


# uvítání

oddelovac = "-----------------------------------------------"
print(f"Hi there! \n{oddelovac} \nI've generated a random 4 digit number for you. \nLet's play a bulls and cows game. \n{oddelovac}")
print("Enter a number:")
print(oddelovac)


# funkce

def je_zdvojene(cislo):
    vysledek = "right input"
    for i in range(len(cislo)):
        for j in range(len(cislo)):
            if i != j and cislo[i] == cislo[j]:
                vysledek = "wrong input"
    return(vysledek)

def bulls_cows(cislo1, cislo2):
    slovnik = {"bull": 0, "cow": 0}
    for i in range(len(cislo1)):
        for j in range(len(cislo2)):
            
            if i == j and cislo1[i] == cislo2[j]:
                slovnik["bull"] += 1
    
            if i != j and cislo1[i] == cislo2[j]:
                slovnik["cow"] += 1

    def jednotne_mnozne(klic1, klic2):
        seznam_novych_klicu = []
        for klic in slovnik:
            if slovnik[klic] > 1 or slovnik[klic] == 0:
                novy_klic = klic + "s"
                seznam_novych_klicu.append(novy_klic)
            else:
                novy_klic = klic
                seznam_novych_klicu.append(novy_klic)
        vysledek = f"{slovnik[klic1]} {seznam_novych_klicu[0]}, {slovnik[klic2]} {seznam_novych_klicu[1]}"
        return(vysledek)
    return(jednotne_mnozne("bull", "cow"))
    
    

# jádro hry

start = time.time()

hra = True
pocet_pokusu = 0
seznam_vyhodnoceni = []

while hra:

    pokus_str = input()
    try:
        pokus = int(pokus_str)
    except ValueError:
        print("The input must contain only digits.")
        print(oddelovac)
    else:
        if len(pokus_str) != 4:
            print("The input must contain exactly 4 digits.")
            print(oddelovac)
        elif pokus_str[0] == "0":
            print("The input must not start with 0")
            print(oddelovac)
        else:
            if je_zdvojene(pokus_str) == "wrong input":
                print("The digits must be unique.")
                print(oddelovac)
            else:
                vyhodnoceni = bulls_cows(tajne_str, pokus_str)
                if vyhodnoceni == "4 bulls, 0 cows":
                    pocet_pokusu += 1
                    seznam_vyhodnoceni.append(vyhodnoceni)
                    if (pocet_pokusu) == 1:
                        print(f"Correct, you've guessed the right number in {pocet_pokusu} guess!")
                    else:
                        print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!")
                    hra = False
                else:
                    print(vyhodnoceni)
                    print(oddelovac)
                    pocet_pokusu += 1
                    seznam_vyhodnoceni.append(vyhodnoceni)
                    
end = time.time()
tvuj_cas_sec = end - start
tvuj_cas_min = tvuj_cas_sec // 60
zbytek_sec = tvuj_cas_sec % 60


print(f"That's amazing!")
for i in range(pocet_pokusu):
    print(f"hra {i + 1}: {seznam_vyhodnoceni[i]}")
print(f"Your time is {tvuj_cas_min:.0f} minutes and {zbytek_sec:.0f} seconds.")
print(oddelovac)