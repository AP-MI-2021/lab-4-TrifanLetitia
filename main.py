def citireLista():
    n=int(input("Dati numarul de siruri al listei: "))
    l = []
    for i in range(0,n):
        nr=str(input("Sirul de pe pozitia" + str(i) + "este:"))
        l.append(nr)
    return l


def gasiresir(l):
    '''
    Determina daca un sir de caractere se gaseste intr-o lista
    :param l: o lista care contine n siruri de caractere
    :return:DA/NU
    '''
    if 'x' in l:
        return True
    else:
        return False
    return True


def siruricareserepeta(l):
    '''
    Afiseaza sirurile de caractere care se repeta intr-o lista
    :param l:o lista care contine n siruri de caractere
    :return: lista1
    '''
    lista1=[]
    for x in l:
        if l.count(x)>=2:
            lista1.append(x)
    lista1=list(dict.fromkeys(lista1))
    return lista1


def test_siruricareserepeta():
    assert siruricareserepeta(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'])==['aaa','bbb']

def isPalindrome(s):
    return s==s[::-1]

def siruriPalindrom(l):
    '''
    Afiseaza sirurile de caractere care sunt palindrom
    :param l: o lista care contine n siruri de caractere
    :return: sirurile care sunt palindrom( o lista)
    '''
    lista3=[]
    for x in l:
        ans=isPalindrome(x)
        if ans:
            lista3.append(x)
    return lista3

def test_siruriPalindrom():
    assert siruriPalindrom(['aaa','fgr','ggh'])==['aaa']


def main():
    l = []
    #test_siruricareserepeta()
    test_siruriPalindrom()
    while True:
        print("1. Citire lista ")
        print("2. Afisare  dacă un șir de caractere citit de la tastatură se găsește în listă")
        print("3. Afișarea listei cu toate șirurile de caractere care se repetă în listă ")
        print("4. Afișarea tuturor șirurilor de caractere din lista care sunt un palindrom. ")
        print("5. Afisarea listeiobtinute prin inlocuirea sirurilor care contin caracterul care apare de cele mai multe ori in toata lista cu numarul de aparitii ale acestui caracter")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            x=str(input("Dati sirul:"))
            if gasiresir(l):
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            if siruricareserepeta(l)!=[]:
                print(siruricareserepeta(l))
            else:
                print("UNIC")

        elif optiune == "4":
            print(siruriPalindrom(l))
        elif optiune == "5":
            print()
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()