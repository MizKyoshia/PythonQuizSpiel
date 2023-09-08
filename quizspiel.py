#Programm für ein Quizspiel
#Autoren: Lukas B. Arthur S., Lucio S.
#Fertigstellung am 08.09.2023

#Definition der Hauptvariablen & Import des random-Pakets
import random
score = 0
rangliste = []

#Fragenkatalog als Python-Dictionary

Hardware = [
    {
        "frage": """Was ist die Hauptfunktion einer CPU? 
        a) Grafikverarbeitung b) Datenepeicherung c) Ausführung von Befehlen""",
        "antwort": "c"
    }, {
        "frage": """Welche Art von Hardware speichert dauerhaft Daten, selbst wenn der Computer ausgeschaltet ist?
        a) RAM b) CPU c) Festplatte""",
        "antwort": "c"
    }, {
        "frage": """Welche Hardware-Komponente ist verantwortlich für die drahtlose Verbindung eines Computers mit dem Internet?
        a) GPU b) Router c) Maus""",
        "antwort": "b"
    }, {
        "frage": """Welche Art von Hardware ermöglicht die Eingabe von Informationen in einen Computer durch Berühren oder Bewegen?
        a) Monitor b) Tastatur c) Touchscreen""",
        "antwort": "c"
    }, {
        "frage": """Welche Hardware-Komponente zeigt Informationen visuell auf einem Bildschirm an?
        a) Festplatte b) GPU (Grafikarte) c) Prozessor""",
        "antwort": "b"
    }
]
Gaming = [
    {
        "frage": """Wie heißt der Protagonist von Red dead Redemption 2?
        a) Arthur Morgan b) Dutch Van der Linde c) John Marston""",
        "antwort": "a"
    }, {
        "frage": """Wie heißen die Hauptfiguren von GTAV?
        a) Michael, John, Trvor b) Michael, Jordan, Jim c) Michael, Trevor, Franklin""",
        "antwort": "c"
    }, {
        "frage": """Welches Spiel gewann den Preis "Game of the Year 2018"?
        a) God of War b) Red Dead Redemption 2 c) Assassins Creed Odyssey""",
        "antwort": "a"
    }, {
        "frage": """Wer sagte den Satz: „Bravo 6 going dark“ in Call of Duty Modern Warfare (2019)?
        a) Soap McTavish b) Ghost c) Captain Price""",
        "antwort": "c"
    }, {
        "frage": """Wann erschien das erste Spiel der Call of Duty Reihe?
        a) 2003 b) 2001 c) 2002""",
        "antwort": "b"
    }
]
Musik = [
    {
        "frage": """Welche Band schrieb das Lied „Paint It Black“?
        a) Die Beatles b) The Rolling Stones c) Elvis Presley""",
        "antwort": "b"
    }, {
        "frage": """Wer spielt bei der Band Rammstein Schlagzeug?
        a) Till Lindemann b) Christoph Walz c) Christoph Schneider""",
        "antwort": "b"
    }, {
        "frage": """Wer war der/die erste Deutschrapper?
        a) Sido b) Die Fantastischen 4 c) Falco""",
        "antwort": "c"
    }, {
        "frage": """Welche Band stellte ihre Musik als Soundtrack für die Transformers Reihe nicht zur Verfügung?
        a) Linkin Park b) Green Day c) AC/DC""",
        "antwort": "c"
    }, {
        "frage": """Wer ist der/die erfolgreichste deutsche Musiker/in in Deutschland?
        a) Helene Fischer b) Peter Mafay c) Herbert Gröhnemeyer""",
        "antwort": "c"
    }
]

#Funktion für die zufällige Auswahl von Fragen aus dem jeweiligen Fragenkatalog
def fragenAuswahl(fragenKatalog):
    global score        #"global" dient der Verwendung der "score" Variable außerhalb der Funktion
    frage = random.choice(fragenKatalog)
    print(frage["frage"])       #Aufrufung der Frage aus dem Fragenkatalog (Python-Dictionary)
    antwort = input("Antwort: ")        

    if antwort == frage["antwort"]:
        print("Richtige Antwort!")
        score +=1
    else:
        print(f"Du liegst leider falsch.Die richtige Antwort wäre '{frage['antwort']}'gewesen!")      #f->als Präfix, damit {} nicht als String ausgegeben werden

#Ranglistenanzeige
def zeigeRangliste():
    print("Rangliste:")
    for eintrag in rangliste:       #"eintrag" dient in der Hauptschleife zur Dokumentierung des Punktestandes & Spielernamen
        print(f"{eintrag['name']} - Punktestand: {eintrag['punkte']}")
    print()

#Hauptschleife
def main():
    global score
    print("Herzlich Willkommen zu unseren Quizspiel!")

    spielername = input("Gib deinen Namen ein, um dich zur Rangliste hinzuzufügen: ")
    rangliste.append({"name": spielername, "punkte": 0})        #Eintrag des Spielernamens in die Rangliste und dessen Punktzahl auf '0'

    while True:
        print("""Bitte wähle aus einem Fragenkatalog aus:
              1) Hardware
              2) Gaming
              3) Musik
              4) Programm beenden
              """)
        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            print("Viel Spaß beim Fragenkatalog zur Hardware!")
            for i in range(5):
                fragenAuswahl(Hardware)         #Ausgabe der Fragen
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")     #Anzeige des scores der aktuell beendeten Spielrunde
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score       #Einschreibung des scores in Rangliste als Punkte
                    break
            zeigeRangliste()
            score = 0

        elif auswahl == "2":
            print("Viel Spaß beim Fragenkatalog zum Gaming!")
            for i in range(5):
                fragenAuswahl(Gaming)           #Ausgabe der Fragen
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")     #Anzeige des scores der aktuell beendeten Spielrunde
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score       #Einschreibung des scores in Rangliste als Punkte
                    break
            zeigeRangliste()
            score = 0

        elif auswahl == "3":
            print("Viel Spaß beim Fragenkatalog zur Musik")
            for i in range(5):
                fragenAuswahl(Musik)            #Ausgabe der Fragen
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")     #Anzeige des scores der aktuell beendeten Spielrunde
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score       #Einschreibung des scores in Rangliste als Punkte
                    break
            zeigeRangliste()
            score = 0
            
        elif auswahl == "4":
            print("""Das Spiel wird nun beendet!
                  Vielen Dank fürs Spielen!""")
            zeigeRangliste()
            break       #Endgültige Beendigung des Programms
        else:
            print("Bitte gib eine richtige Ziffer ein!")

main()