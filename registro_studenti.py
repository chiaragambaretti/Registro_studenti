studenti = ['Bianchi Flavio', 'Rossi Maria', 'Gambaretti Chiara']
valutazioni = [
    [7.5, 5, 9],
    [5, 8.5],
    [8, 7.5]
]

azioni = [
    'Mostra elenco studenti',
    'Mostra il registro completo',
    'Mostra i voti di uno studente',
    'Mostra le medie degli studenti',
    'Mostra la media di tutti i voti',
    'Mostra il voto più alto di ciascuno studente',
    'Mostra i voti insufficienti',
    'Salva i dati su file',
    'Carica i dati da file',
    'Aggiungi uno studente',
    'Elimina uno studente',
    'Registra un voto',
    'Elimina un voto',
    'Elimina tutti gli studenti'
]


# Funzioni supporto

def mostra_studenti():
    """Mostra l'elenco degli studenti."""
    if not studenti:
        print("Nessuno studente presente.")
        return False
    for i, studente in enumerate(studenti, start=1):
        print(f"{i}. {studente}")
    return True


def mostra_registro():
    """Mostra l'intero registro studenti + voti."""
    if not studenti:
        print("Nessuno studente presente.")
    else:
        for studente, voti in zip(studenti, valutazioni):
            print(f"{studente}: {voti if voti else 'nessuna valutazione'}")


def media(voti):
    """Restituisce la media di una lista di voti."""
    return sum(voti) / len(voti) if voti else 0


# Funzioni operazioni

def mostra_voti_studente():
    if not mostra_studenti():
        return
    indice = int(input("Seleziona lo studente: ")) - 1
    voti = valutazioni[indice]
    if voti:
        print(f"{studenti[indice]}: {', '.join(map(str, voti))}")
    else:
        print("Questo studente non ha ancora valutazioni.")


def mostra_medie_studenti():
    if not studenti:
        print("Nessuno studente presente.")
    else:
        for studente, voti in zip(studenti, valutazioni):
            print(f"{studente}: media {media(voti):.2f}" if voti else f"{studente}: nessuna valutazione")


def mostra_media_totale():
    tutti_i_voti = [v for lista in valutazioni for v in lista]
    if tutti_i_voti:
        print(f"La media di tutti i voti è: {media(tutti_i_voti):.2f}")
    else:
        print("Non ci sono voti registrati.")


def mostra_voto_massimo():
    if not studenti:
        print("Nessuno studente presente.")
    else:
        for studente, voti in zip(studenti, valutazioni):
            print(f"{studente}: voto più alto = {max(voti)}" if voti else f"{studente}: nessuna valutazione")


def mostra_voti_insufficienti():
    if not studenti:
        print("Nessuno studente presente.")
    else:
        for studente, voti in zip(studenti, valutazioni):
            insufficienti = [v for v in voti if v < 6]
            print(f"{studente}: voti insufficienti = {insufficienti}" if insufficienti else f"{studente}: nessun voto insufficiente")


def aggiungi_studente():
    nome = input("Inserisci il nome dello studente: ").strip()
    cognome = input("Inserisci il cognome dello studente: ").strip()
    if not nome or not cognome:
        print("Nome o cognome non validi.")
        return
    nuovo_studente = f"{cognome.capitalize()} {nome.capitalize()}"
    studenti.append(nuovo_studente)
    valutazioni.append([])
    studenti.sort()
    # Riordina valutazioni in parallelo
    studenti_valutazioni = sorted(zip(studenti, valutazioni))
    studenti[:], valutazioni[:] = zip(*studenti_valutazioni)
    print(f"Studente {nuovo_studente} aggiunto con successo.")


def elimina_studente():
    if not mostra_studenti():
        return
    indice = int(input("Scegli lo studente da eliminare: ")) - 1
    conferma = input(f"Sei sicuro di voler eliminare {studenti[indice]}? (s/n): ").lower()
    if conferma == 's':
        eliminato = studenti.pop(indice)
        valutazioni.pop(indice)
        print(f"Studente '{eliminato}' eliminato correttamente.")
    else:
        print("Operazione annullata.")


def registra_voto():
    if not mostra_studenti():
        return
    indice = int(input("Scegli lo studente: ")) - 1
    voto = float(input("Inserisci il voto (da 0 a 10): "))
    if 0 <= voto <= 10:
        valutazioni[indice].append(voto)
        print(f"Voto {voto} aggiunto per {studenti[indice]}.")
    else:
        print("Voto non valido.")


def elimina_voto():
    if not mostra_studenti():
        return
    indice = int(input("Scegli lo studente: ")) - 1
    voti = valutazioni[indice]
    if not voti:
        print("Questo studente non ha voti.")
        return
    for i, voto in enumerate(voti, start=1):
        print(f"{i}. {voto}")
    num_voto = int(input("Quale voto vuoi eliminare?: ")) - 1
    if 0 <= num_voto < len(voti):
        rimosso = voti.pop(num_voto)
        print(f"Voto {rimosso} rimosso correttamente.")
    else:
        print("Numero voto non valido.")


def elimina_tutti():
    conferma = input("Sei sicuro di voler eliminare TUTTI gli studenti? (s/n): ").lower()
    if conferma == 's':
        studenti.clear()
        valutazioni.clear()
        print("Tutti gli studenti e le loro valutazioni sono stati eliminati.")
    else:
        print("Operazione annullata.")


def salva_file():
    if not studenti:
        print("Nessuno studente presente. Salvataggio non effettuato.")
        return
    nome_file = input("Nome del file (senza estensione): ").strip()
    with open(f"{nome_file}.txt", "w") as file:
        for studente, voti in zip(studenti, valutazioni):
            file.write(f"{studente}: {', '.join(map(str, voti))}\n")
    print("Dati salvati correttamente.")


def carica_file():
    nome_file = input("Nome del file da caricare (senza estensione): ").strip()
    try:
        with open(f"{nome_file}.txt", "r") as file:
            studenti.clear()
            valutazioni.clear()
            for riga in file:
                if ":" not in riga:
                    continue
                nome, voti_str = riga.strip().split(":", 1)
                try:
                    voti = [float(v) for v in voti_str.split(",") if v.strip()]
                except ValueError:
                    voti = []
                studenti.append(nome.strip())
                valutazioni.append(voti)
        print("Dati caricati correttamente.")
    except FileNotFoundError:
        print("File non trovato.")


# Ciclo principale

azioni_funzioni = {
    1: mostra_studenti,
    2: mostra_registro,
    3: mostra_voti_studente,
    4: mostra_medie_studenti,
    5: mostra_media_totale,
    6: mostra_voto_massimo,
    7: mostra_voti_insufficienti,
    8: salva_file,
    9: carica_file,
    10: aggiungi_studente,
    11: elimina_studente,
    12: registra_voto,
    13: elimina_voto,
    14: elimina_tutti
}

while True:
    print("\n----- MENU -----")
    for i, azione in enumerate(azioni, start=1):
        print(f"{i}. {azione}")
    print("----------------")

    selezione = input("Inserisci il numero corrispondente all'azione: ").strip()
    if not selezione.isdigit() or not (1 <= int(selezione) <= len(azioni)):
        print("Scelta non valida.")
        continue

    selezione = int(selezione)
    print(f"\nHai scelto: {azioni[selezione - 1]}\n")

    azioni_funzioni[selezione]()  # Esegue la funzione corrispondente

    ripeti = input("\nVuoi eseguire un'altra operazione? (s/n): ").lower()
    if ripeti != 's':
        print("Uscita dal programma.")
        break