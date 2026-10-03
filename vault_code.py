import random

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_BASE = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""

    if tentativo<codice:
        return "più alto"
    else:
        return "più basso"

def stampa_tentativi(n, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    rimasti=n-usati
    print("X"*usati+"0"*rimasti)


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    n = TENTATIVI_BASE - livello
    if n < TENTATIVI_MIN:
        n = TENTATIVI_MIN
    codice = random.randint(CODICE_MIN, CODICE_MAX)
    usati = 0
    while usati<n:
        stampa_tentativi(n, usati)
        tentativo=int(input("inserisci il codice: "))
        usati+=1
        if tentativo==codice:
            print("hai vinto")
            return True
        else:
            print(dai_indizio(tentativo, codice))

    print("tentativi esauriti: hai perso")
    return False






def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
