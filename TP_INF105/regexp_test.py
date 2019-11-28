

depart = 0
arrivee = 0
dico = dict()
langages = []
regexp = ""

for i in range(7):  # état, classe de congruence
    for j in range(10) : # 10 chiffres à ajouter
        dico[(i,j)] = (i*10 + j)%7


def est_dans_L_tableau(T) :
    etat = depart
    for chiffre in T :
        etat = dico[(etat, chiffre)]

    return etat == arrivee

def est_dans_L(nombre):
    T = [int(c) for c in str(nombre)]
    return est_dans_L_tableau(T)


def init_L(k):
    T = []
    for i in range(7): # etat
        for j in range(10) :
            if dico[(i,j)] == k :
                T.append((str(j), i))
    return T

def init() :
    global langages
    langages = [init_L(k) for k in range(7)]

init()

def parenthèses_autour(exp):
    pile = [exp[0]]
    if exp[0] != "(" or exp[-1] != ")" :
        return False

    for c in exp[1:-1] :
        if c == "(" :
            pile.append(c)
        if c == ")" and pile :
            pile.pop()
        if pile == [] :
            return False

    if len(pile) == 1:
        return True
    else :
        print("WALA Y A UN PB")




def entoure(exp):
    if len(exp) <= 1 or parenthèses_autour(exp):
        return exp
    else :
        return "("+exp+")"

def simplifie_L(k):
    L = langages[k]
    expL = ""

    for (exp, j) in L :
        if j == k :
            if expL :
                expL += "|" + exp
            else :
                expL = exp

    if expL :
        langages[k] = [ (exp + entoure(expL) + "*", j) for (exp, j) in L if j != k]



def regroupe_les_i_dans_Lk(i,k):

    L = langages[k]
    expL = ""

    for (exp, j) in L :
        if j == i:
            if expL :
                expL += "|" + entoure(exp)
            else :
                expL = entoure(exp)

    if expL :
        langages[k] = [(exp,j) for (exp,j) in L if j != i] + [(entoure(expL),i)]



def remplace_i_dans_Lk(i,k):

    L = langages[k]
    expL = ""

    for (exp,j) in L:
        if j == i :
            expL = exp


    langages[k] = [(exp,j) for (exp,j) in L if j != i] + [ (entoure(exp) + entoure(expL), j)
                    for (exp,j) in langages[i]]


def simplifie(ligne) :

    for i in range(7) :
        regroupe_les_i_dans_Lk(i,ligne)


def main():

    for ligne in range(7) :
        simplifie(ligne)

    for aElimine in range(6,0,-1):  # Pas le 0 !
        simplifie_L(aElimine)
        for ligne in range(0,aElimine):
            remplace_i_dans_Lk(aElimine,ligne)
            simplifie(ligne)


main()

regexp = "^(" + langages[0][0][0] + ")*$"


text_file = open("regexp.txt", "w")
n = text_file.write(regexp)
text_file.close()





