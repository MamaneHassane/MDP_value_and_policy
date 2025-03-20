import numpy as np

# Paramètres du problème
n, m = 3, 4  # n lignes, m colonnes
gamma = 0.9  # Facteur d'escompte
epsilon = 1e-4  # Critère d'arrêt

# Actions possibles (Droite, Gauche, Haut, Bas)
actions = {'→': (0, 1), '←': (0, -1), '↑': (1, 0), '↓': (-1, 0)}

# États terminaux et états interdits
etats_terminaux = {(1, 3): -1, (2, 3): 1}
etats_interdits = {(1, 1)}

# Initialisation des récompenses
R = np.zeros((n, m))
for (ligne, colonne), recompense in etats_terminaux.items():
    R[ligne, colonne] = recompense

# Vérifier si un état est valide
def est_valide(ligne, colonne):
    return (0 <= ligne < n and 0 <= colonne < m and (ligne, colonne) not in etats_interdits)

# Fonction de transition
def transitions(ligne, colonne, action):
    d_ligne, d_col = actions[action]
    principal = (ligne + d_ligne, colonne + d_col)

    lateraux = {
        '→': [('↑', 0.1), ('↓', 0.1)],
        '←': [('↑', 0.1), ('↓', 0.1)],
        '↑': [('←', 0.1), ('→', 0.1)],
        '↓': [('←', 0.1), ('→', 0.1)]
    }

    resultats = []
    #
    resultats.append((principal if est_valide(*principal) else (ligne, colonne), 0.8))

    for action_lat, prob in lateraux[action]:
        d_lat_ligne, d_lat_col = actions[action_lat]
        lateral = (ligne + d_lat_ligne, colonne + d_lat_col)
        resultats.append((lateral if est_valide(*lateral) else (ligne, colonne), prob))

    return resultats

# Algorithme d'itération de la valeur
def iteration_valeur():
    V = np.zeros((n, m))
    for s in etats_interdits: V[s] = np.nan
    for s in etats_terminaux: V[s] = etats_terminaux[s]

    while True:
        delta = 0
        V_nouveau = V.copy()
        for ligne in range(n):
            for colonne in range(m):
                if (ligne, colonne) in etats_terminaux or (ligne, colonne) in etats_interdits:
                    continue
                valeur_max = -np.inf
                for a in actions:
                    valeur = sum(p * (R[s] + gamma * V[s]) for s, p in transitions(ligne, colonne, a))
                    valeur_max = max(valeur_max, valeur)
                delta = max(delta, abs(V[ligne, colonne] - valeur_max))
                V_nouveau[ligne, colonne] = valeur_max
        V = V_nouveau
        if delta < epsilon:
            break
    return V

# Algorithme d'itération de la politique
def iteration_politique():
    V = np.zeros((n, m))
    politique = np.full((n, m), ' ')

    for s in etats_interdits:
        V[s] = np.nan
        politique[s] = 'X'

    for s in etats_terminaux:
        V[s] = etats_terminaux[s]
        politique[s] = 'T'

    stable = False
    while not stable:
        # Évaluation
        while True:
            delta = 0
            V_nouveau = V.copy()
            for ligne in range(n):
                for colonne in range(m):
                    if politique[ligne, colonne] in (' ', 'X', 'T'):
                        continue
                    valeur = sum(p * (R[s] + gamma * V[s]) for s, p in transitions(ligne, colonne, politique[ligne, colonne]))
                    delta = max(delta, abs(V[ligne, colonne] - valeur))
                    V_nouveau[ligne, colonne] = valeur
            V = V_nouveau
            if delta < epsilon:
                break

        # Amélioration
        stable = True
        for ligne in range(n):
            for colonne in range(m):
                if (ligne, colonne) in etats_terminaux or (ligne, colonne) in etats_interdits:
                    continue
                meilleure_action, meilleure_valeur = None, -np.inf
                for a in actions:
                    valeur = sum(p * (R[s] + gamma * V[s]) for s, p in transitions(ligne, colonne, a))
                    if valeur > meilleure_valeur:
                        meilleure_valeur, meilleure_action = valeur, a
                if politique[ligne, colonne] != meilleure_action:
                    stable = False
                    politique[ligne, colonne] = meilleure_action

    return V, politique

# Exécution des algorithmes
V_valeur = iteration_valeur()
V_politique, politique = iteration_politique()

# Affichage des résultats
print("\nValeurs optimales (Itération de la Valeur):")
for ligne in reversed(range(n)):
    print([f"{V_valeur[ligne, col]:.2f}" if not np.isnan(V_valeur[ligne, col]) else "X" for col in range(m)])

print("\nValeurs optimales (Itération de la Politique):")
for ligne in reversed(range(n)):
    print([f"{V_politique[ligne, col]:.2f}" if not np.isnan(V_politique[ligne, col]) else "X" for col in range(m)])

print("\nPolitique optimale finale:")
for ligne in reversed(range(n)):
    print([politique[ligne, col] for col in range(m)])
