def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")

print("Entrer nom du joueur 1")
joueur1=input()
print("Entrer nom du joueur 2")
joueur2=input()
def tour(grille, joueur1 , joueur2):
    print("C'est le tour du joueur "+str(joueur1 or joueur2))
    colonne=input("Entrez le numero de la colonne : ")
    ligne=input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case ("+colonne+","+ligne+")")
    while grille[int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")

    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_grille(grille)

def est_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1


def est_match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1

joueur=1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
grille=[" "," "," "," "," "," "," "," "," "]
afficher_grille(grille)
gagne=0
while gagne==0:
    tour(grille,joueur1,joueur2)
    if est_gagnant(grille):
        print("Le joueur "+str(joueur)+" remporte la partie")
        gagne=1
    else:
        if est_match_nul(grille):
            print("Plus de place ! Match nul !")
            gagne=1            
    if joueur==1:
        joueur=2
    else:
        joueur=1
score=gagne
file = open("score.txt", "w") 
j1=joueur1
j2=joueur2
a=score
if j1 == a :
    print(a)
elif j2 != a :
    print(a-1)
file.write(j1+","+str(a)+"\n"+j2+","+str(a-1))
file.close()