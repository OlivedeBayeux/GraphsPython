import numpy as np

class Pile:
    def __init__(self):
        self.liste = []

    def push(self, element):
        self.liste.append(element)

    def pop(self):
        return self.liste.pop()

    def isEmpty(self):
        if len(self.liste) == 0:
            return 1
        return 0

    def clear(self):
        self.liste.clear()

    # obtenir le dernier élément sans le retirer de la pile
    def last(self):
        return self.liste[len(self.liste) - 1]


#afficher la matrice avec format sans virgule pour les nombres entiers
def matbin_afficher(mat, n):

    i = 0
    print("  ", end = '')
    while i < n:
        print("--", end = '')
        i = i + 1
    print("-")

    i = 0
    for l in mat:
        print('|', end = '')
        is_debut = 1
        for e in l:
            if is_debut == 1:
                is_debut = 0
            else:
                print(' ', end='')

            print (int(e), end='')

        print('|')
        i = i  + 1

    i = 0
    print("  ", end = '')
    while i < n:
        print("--", end = '')
        i = i + 1
    print("-")


class Graphe_np:
    def __init__(self, nb_sommets, noms_sommets):
        self.sommets = []
        self.arcs = []
        self.sommets_value = []
        self.pile = Pile()
        self.ordre_previsite = []
        self.ordre_postvisite = []


        self.matrice = np.zeros( (nb_sommets,nb_sommets), dtype=np.bool_ )
        self.nb_sommets = nb_sommets

        self.sommets = noms_sommets.copy()

         #init des valeurs des sommets à 0 et création de la liste
        i = 0
        while i < nb_sommets:
            self.sommets_value.append(0)
            i = i + 1


    #afficher la matrice avec format sans virgule pour les nombres entiers
    def afficher(self):

        #afficher ligne labelle
        i = 0
        print("  ",  end = '')
        while i < self.nb_sommets:
            print(" ", self.sommets[i], sep = '', end = '')

            i = i + 1
        print("")

        i = 0
        print("  ", end = '')
        while i < self.nb_sommets:
            print("--", end = '')
            i = i + 1
        print("-")

        i = 0
        for l in self.matrice:
            print(self.sommets[i], '|', end = '')
            is_debut = 1
            for e in l:
                if is_debut == 1:
                    is_debut = 0
                else:
                    print(' ', end='')

                print (int(e), end='')

            print('|')
            i = i  + 1

        i = 0
        print("  ", end = '')
        while i < self.nb_sommets:
            print("--", end = '')
            i = i + 1
        print("-")

    # obtenir l'indice d'un sommet depuis son nom
    def get_ind_sommet(self, label):
        i = 0
        while i < self.nb_sommets:
            if self.sommets[i] == label:
                return i
            i = i + 1
        return -1

    def init_sommets_value(self, value):
        #initialiser tous els sommets à la valeur 'value'
        i = 0
        while(i < self.nb_sommets):
            self.sommets_value[i] = value
            i = i + 1

    def set_sommet_value(self, label_sommet, value):
        i = self.get_ind_sommet(label_sommet)
        if i == -1:
            return False

        self.sommets_value[i] = value
        return True

    def get_sommet_value(self, label_sommet):
        i = self.get_ind_sommet(label_sommet)
        if i == -1:
            return False

        return self.sommets_value[i]

    #ajouter un arc depuis le nom de 2 sommets
    def add_arc(self, label_sommet1, label_sommet2):
        i = 0
        ind_s1 = self.get_ind_sommet(label_sommet1)
        ind_s2 = self.get_ind_sommet(label_sommet2)

        self.arcs.append([self.sommets[ind_s1],self.sommets[ind_s2]])
        self.matrice[ind_s1][ind_s2] = True

    # ajouter une liste d'arcs [["A","B"],["A","C"],...]
    def add_arcs(self, liste_arcs):
        for arc in liste_arcs:
            self.add_arc(arc[0], arc[1])


    # successeur d'un nom de sommet
    def successeur(self, label_sommet):
        M = self.matrice
        n = self.nb_sommets
        ind = self.get_ind_sommet(label_sommet)

        liste = []

        i = 0
        while (i < n ):
            if (M [ind][i] == True ):
                #print(i)
                liste.append(self.sommets[i])
            i = i + 1
        return liste

    # predecesseur d'un nom de sommet
    def predecesseur(self, label_sommet):
        M = self.matrice
        n = self.nb_sommets
        ind = self.get_ind_sommet(label_sommet)

        liste = []

        i = 0
        while (i < n ):
            if (M [i][ind] == True):
                #print(i)
                liste.append(self.sommets[i])
            i = i + 1

        return liste

G = Graphe_np(6,["A","B","C","D","E","F","G","H"])
G.add_arcs([["A","B"],["A","C"],["B","F"],["F","C"],["F","G"]])
G.add_arcs([["E","A"],["E","D"],["D","H"],["H","D"]])

G.afficher();
