import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# ===========================
# Dati iniziali
# ===========================
studenti = ['Bianchi Flavio', 'Rossi Maria', 'Gambaretti Chiara']
valutazioni = [
    [7.5, 5, 9],
    [5, 8.5],
    [8, 7.5]
]

# Funzioni di supporto

def media(voti):
    return sum(voti)/len(voti) if voti else 0


# Funzioni GUI

def mostra_studenti_gui():
    if not studenti:
        messagebox.showinfo("Studenti", "Nessuno studente presente.")
        return
    lista = "\n".join([f"{i+1}. {s}" for i, s in enumerate(studenti)])
    messagebox.showinfo("Elenco studenti", lista)

def mostra_registro_gui():
    if not studenti:
        messagebox.showinfo("Registro", "Nessuno studente presente.")
        return
    registro = ""
    for s, v in zip(studenti, valutazioni):
        registro += f"{s}: {v if v else 'nessuna valutazione'}\n"
    messagebox.showinfo("Registro completo", registro)

def mostra_voti_studente_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    scelta = simpledialog.askinteger("Seleziona studente",
                                     "\n".join([f"{i+1}. {s}" for i, s in enumerate(studenti)]))
    if scelta and 1 <= scelta <= len(studenti):
        voti = valutazioni[scelta-1]
        msg = ', '.join(map(str, voti)) if voti else "nessuna valutazione"
        messagebox.showinfo("Voti Studente", f"{studenti[scelta-1]}: {msg}")
    else:
        messagebox.showerror("Errore", "Studente non valido.")

def mostra_medie_studenti_gui():
    if not studenti:
        messagebox.showinfo("Medie", "Nessuno studente presente.")
        return
    testo = ""
    for s, v in zip(studenti, valutazioni):
        testo += f"{s}: {media(v):.2f}\n" if v else f"{s}: nessuna valutazione\n"
    messagebox.showinfo("Medie studenti", testo)

def mostra_media_totale_gui():
    tutti = [v for lista in valutazioni for v in lista]
    if tutti:
        messagebox.showinfo("Media totale", f"Media di tutti i voti: {media(tutti):.2f}")
    else:
        messagebox.showinfo("Media totale", "Nessun voto registrato.")

def mostra_voto_massimo_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    testo = ""
    for s, v in zip(studenti, valutazioni):
        testo += f"{s}: massimo {max(v)}\n" if v else f"{s}: nessuna valutazione\n"
    messagebox.showinfo("Voto massimo", testo)

def mostra_voti_insufficienti_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    testo = ""
    for s, v in zip(studenti, valutazioni):
        insufficienti = [x for x in v if x < 6]
        testo += f"{s}: {insufficienti}\n" if insufficienti else f"{s}: nessun voto insufficiente\n"
    messagebox.showinfo("Voti insufficienti", testo)

def aggiungi_studente_gui():
    nome = simpledialog.askstring("Nome", "Inserisci il nome:")
    cognome = simpledialog.askstring("Cognome", "Inserisci il cognome:")
    if nome and cognome:
        nuovo_studente = f"{cognome.capitalize()} {nome.capitalize()}"
        studenti.append(nuovo_studente)
        valutazioni.append([])
        studenti_valutazioni = sorted(zip(studenti, valutazioni))
        studenti[:], valutazioni[:] = zip(*studenti_valutazioni)
        messagebox.showinfo("Successo", f"Studente {nuovo_studente} aggiunto.")

def elimina_studente_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    scelta = simpledialog.askinteger("Seleziona studente",
                                     "\n".join([f"{i+1}. {s}" for i, s in enumerate(studenti)]))
    if scelta and 1 <= scelta <= len(studenti):
        if messagebox.askyesno("Conferma", f"Eliminare {studenti[scelta-1]}?"):
            studenti.pop(scelta-1)
            valutazioni.pop(scelta-1)
            messagebox.showinfo("Eliminato", "Studente eliminato con successo.")
    else:
        messagebox.showerror("Errore", "Studente non valido.")

def registra_voto_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    scelta = simpledialog.askinteger("Seleziona studente",
                                     "\n".join([f"{i+1}. {s}" for i, s in enumerate(studenti)]))
    if scelta and 1 <= scelta <= len(studenti):
        voto = simpledialog.askfloat("Voto", "Inserisci il voto (0-10):")
        if voto is not None and 0 <= voto <= 10:
            valutazioni[scelta-1].append(voto)
            messagebox.showinfo("Successo", f"Voto {voto} aggiunto a {studenti[scelta-1]}.")
        else:
            messagebox.showerror("Errore", "Voto non valido.")
    else:
        messagebox.showerror("Errore", "Studente non valido.")

def elimina_voto_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    scelta = simpledialog.askinteger("Seleziona studente",
                                     "\n".join([f"{i+1}. {s}" for i, s in enumerate(studenti)]))
    if scelta and 1 <= scelta <= len(studenti):
        voti = valutazioni[scelta-1]
        if not voti:
            messagebox.showinfo("Errore", "Questo studente non ha voti.")
            return
        voto_scelto = simpledialog.askinteger("Seleziona voto",
                                              "\n".join([f"{i+1}. {v}" for i, v in enumerate(voti)]))
        if voto_scelto and 1 <= voto_scelto <= len(voti):
            rimosso = voti.pop(voto_scelto-1)
            messagebox.showinfo("Successo", f"Voto {rimosso} eliminato.")
        else:
            messagebox.showerror("Errore", "Voto non valido.")
    else:
        messagebox.showerror("Errore", "Studente non valido.")

def elimina_tutti_gui():
    if messagebox.askyesno("Conferma", "Eliminare tutti gli studenti?"):
        studenti.clear()
        valutazioni.clear()
        messagebox.showinfo("Eliminato", "Tutti gli studenti eliminati.")

def salva_file_gui():
    if not studenti:
        messagebox.showinfo("Errore", "Nessuno studente presente.")
        return
    nome_file = filedialog.asksaveasfilename(defaultextension=".txt")
    if nome_file:
        with open(nome_file, "w") as f:
            for s, v in zip(studenti, valutazioni):
                f.write(f"{s}: {', '.join(map(str,v))}\n")
        messagebox.showinfo("Salvataggio", "Dati salvati correttamente.")

def carica_file_gui():
    nome_file = filedialog.askopenfilename(defaultextension=".txt")
    if nome_file:
        try:
            studenti.clear()
            valutazioni.clear()
            with open(nome_file, "r") as f:
                for riga in f:
                    if ":" not in riga:
                        continue
                    s, v_str = riga.strip().split(":",1)
                    v = [float(x) for x in v_str.split(",") if x.strip()]
                    studenti.append(s.strip())
                    valutazioni.append(v)
            messagebox.showinfo("Caricamento", "Dati caricati correttamente.")
        except:
            messagebox.showerror("Errore", "Impossibile caricare il file.")


# GUI principale

root = tk.Tk()
root.title("Registro Studenti")
root.geometry("400x600")

tk.Label(root, text="Registro Studenti", font=("Arial", 16)).pack(pady=10)

# Bottoni per tutte le operazioni
tk.Button(root, text="Mostra studenti", width=30, command=mostra_studenti_gui).pack(pady=5)
tk.Button(root, text="Mostra registro completo", width=30, command=mostra_registro_gui).pack(pady=5)
tk.Button(root, text="Mostra voti di uno studente", width=30, command=mostra_voti_studente_gui).pack(pady=5)
tk.Button(root, text="Mostra medie studenti", width=30, command=mostra_medie_studenti_gui).pack(pady=5)
tk.Button(root, text="Mostra media di tutti i voti", width=30, command=mostra_media_totale_gui).pack(pady=5)
tk.Button(root, text="Mostra voto massimo di ciascuno", width=30, command=mostra_voto_massimo_gui).pack(pady=5)
tk.Button(root, text="Mostra voti insufficienti", width=30, command=mostra_voti_insufficienti_gui).pack(pady=5)
tk.Button(root, text="Aggiungi studente", width=30, command=aggiungi_studente_gui).pack(pady=5)
tk.Button(root, text="Elimina studente", width=30, command=elimina_studente_gui).pack(pady=5)
tk.Button(root, text="Registra un voto", width=30, command=registra_voto_gui).pack(pady=5)
tk.Button(root, text="Elimina un voto", width=30, command=elimina_voto_gui).pack(pady=5)
tk.Button(root, text="Elimina tutti gli studenti", width=30, command=elimina_tutti_gui).pack(pady=5)
tk.Button(root, text="Salva dati su file", width=30, command=salva_file_gui).pack(pady=5)
tk.Button(root, text="Carica dati da file", width=30, command=carica_file_gui).pack(pady=5)
tk.Button(root, text="Esci", width=30, command=root.destroy).pack(pady=20)

root.mainloop()

