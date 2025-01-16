#!/usr/bin/env python
# -*- coding: utf-8 -*

def syracuseFunc(n):
    if n < 0:
        return "please enter a positiv number"
    else:
        num = n
        result = []
        result.append(num)

        while num > 1:
            if num % 2 == 0:
                num = num / 2
                print(f"{num}")
                result.append(num)
            else:
                num = (num * 3) + 1
                print(f"{num}")
                result.append(num)
        return result

if __name__ == '__main__':
    try:
        nb = float(input("Entrer un nombre entier positif : "))
        fact_nb = syracuseFunc(nb)
        print(f"le resultat total est : {fact_nb} , {nb} etant le nombre de depart")
    except ValueError:
        print("ceci n'est pas correcte ressayer ! ")