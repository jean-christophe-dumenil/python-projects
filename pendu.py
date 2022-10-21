import random
with open('dico_france.txt', "r", encoding= "iso-8859-1") as f:
     toto = f.readlines()
solution = random.choice(toto)

choix = int(input("Veuillez choisir le niveau de difficulté facile = 1, moyen = 2, difficile = 3 ? : "))

print(">> Bienvenue dans le pendu <<")

if choix == 2:
    tentatives = 7
    lettre = []
elif choix == 1:
    tentatives = 10
    lettre = []
elif choix == 3:
    tentatives = 4
    lettre = []
affichage = ""
lettres_trouvees = ""

for l in solution:
    affichage = affichage + "_ "

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")
  lettre.append(proposition)
  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print(tentatives)
    print(lettre)
    if tentatives==0:
        print("perdue")       
    elif tentatives<=1:      
        print("perdue")
    elif tentatives<=2:
        print("perdue")
    elif tentatives<=3:
        print("perdue")
    elif tentatives<=4:
        print("perdue")
    elif tentatives<=5:                    
        print("perdue")     
    elif tentatives<=6:
        print("perdue")
  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")


for l in solution:
  affichage = affichage + "_ "

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print(tentatives)
    print(lettre)
    if tentatives==0: 
        print("perdue")
    elif tentatives<=1:
        print("perdue")
    elif tentatives<=2:
        print("perdue")
    elif tentatives<=4:
        print("perdue")
    elif tentatives<=5:                    
        print("perdue")
    elif tentatives<=6:                    
        print("perdue")
    elif tentatives<=7:                    
        print("perdue")
    elif tentatives<=8:                    
        print("perdue")
    elif tentatives<=9:
        print("perdue")


  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     

affichage = ""
lettres_trouvees = ""

for l in solution:
    affichage = affichage + "_ "

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print(tentatives)
    print(lettre)
    if tentatives==0:
        print("perdue")
    elif tentatives<=1:
        print("perdue")
    elif tentatives<=2:
        print("perdue")
    elif tentatives<=3:
        print("perdue")
    elif x in lettres_trouvees:
          affichage += x + " "
    else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break