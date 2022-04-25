# programme Polynome (seance 1, exo 1-2-3)
# 25/04/22
choix = "O"
while choix == "O": # grande boucle contenant tout le programme
    n = 7
    while n > 6:
        n = int(input("Entrez le degré du polynôme (maximum 6) = "))
    a = []
    for k in range(0, n + 1):
        a.append(float(input("a" + str(k) + "= ")))
    for k in range(1, n + 1):
        if a[k] != 0:
            print("f(x) = ",a[0]," + ", a[k], " * x^", k)
    while choix == "O": # boucle saisie d'un nouveau nombre
        x = int(input("saisir x = "))
        resultat = 0
        for k in range(0, n + 1):
            resultat = resultat + a[k] * pow(x,k)
            print("f(x) = ",resultat)
        choix = input("Voulez vous saisir un nouveau x ? (O/N) : ")
    choix = input("voulez vous saisir un nouveau polynome? (O/N) : ")
