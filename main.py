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
    lista1=[]
    for x in l:
        if l.count(x)>=2:
            lista1.append(x)
    lista1=list(dict.fromkeys(lista1))
    return lista1


def test_siruricareserepeta():
    assert siruricareserepeta(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'])==['aaa','bbb']


def main():
    l = []
    #test_siruricareserepeta()
    while True:
        print("1. Citire lista ")
        print("2. Afisare  dacă un șir de caractere citit de la tastatură se găsește în listă")
        print("3. ")
        print("4. ")
        print("5. ")
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
            print()
        elif optiune == "5":
            print()
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()