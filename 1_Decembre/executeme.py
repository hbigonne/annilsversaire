from file import module

########## MAIN


def game(mode):
    console=mode.split()
    cumul=""
    for i in console :
        word_fund = False
        print(" "*len("Ta proposition ? ")+"x"*len(i))
        

        while word_fund == False :
            a =input("Ta proposition ? ")
            while len(a) != len(i):
                print(f"Mais regarde bien, il y a {len(i)} caractères")
                print(" "*len("Ta proposition ? ")+"x"*len(i))
                a =input("Ta proposition ? ")
            out=""
            read =0
            while read< len(i):
                if a[read] == i[read]:
                    out+=a[read]
                elif a[read] in i :
                    out+=("*")
                else :
                    out+=("_")
                read+=1
            print(" "*len("Ta proposition ? ")+out)
            if out == i:
                word_fund = True
                print("ouiiiiii c'est ça!")
                print(" ")
            else :
                print("try again")
                print("")
                

        cumul+=a+" "
        print(cumul)
        print("")

############ call

print("bienvenü")
print("")
print("ceci est un jeu, comme le master mind ou le wordle")
print("le but est de deviner une courte séquence de mots")
print("en retrouvant les lettres de chaque mot ainsi que leur position")
print("il n'y a pas de nombre limite de tentatives")
print("")
print("tout est en minuscule, pas d'accents, chiffres ou caractères spéciaux")
print("si la lettre est trouvée à la bonne place, elle est affichée dans la réponse")
print("si la lettre est trouvée à la mauvaise place, un * apparaît")
print("si la lettre n'est pas dans le mot, un _ apparaît")
print("attention : il y a une lettre en double dans le premier mot")
print("ah oui et fais gaffe à pas taper d'espace, ça m'a fait chier")
print("")
game(module)
print("Waow t'es le plus fort tu mérites tes 25 cadeaux alors")
print("Ah et y a pas d'histoire de photos à imprimer, promis :p")




