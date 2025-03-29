
import streamlit as st

# Titel der App
st.title('Operative Durcharbeitung & Kognitive Aktivierung (Mittelschule)')

# Einführung
st.markdown('''
In dieser App lernen Sie, wie Sie operative Durcharbeitung und kognitive Aktivierung im Mathematikunterricht der Mittelschule fördern können.

### Zielsetzungen:
- Förderung von Problemlösekompetenzen
- Förderung der Fähigkeit, mathematische Sachverhalte zu begründen
- Förderung der Modellierungskompetenzen
''')

# Problemlösen
st.header('1. Problemlösen – komplexe Sachaufgaben zur Prozentrechnung')

st.markdown('''
**Beispielaufgabe:**

Ein Pullover kostet ursprünglich 40 Euro. Während eines Sonderverkaufs wird der Preis zuerst um 20% gesenkt. Danach gibt es zusätzlich 10% Rabatt auf den bereits reduzierten Preis. 

**Aufgabe:** Wie viel kostet der Pullover am Ende?
''')

preis = 40
erste_reduktion = preis * (1 - 0.20)
zweite_reduktion = erste_reduktion * (1 - 0.10)

if st.button('Lösung anzeigen'):
    st.success(f'Der Pullover kostet am Ende {zweite_reduktion:.2f} Euro.')

st.markdown('''
**Aufgabe für Sie:** Formulieren Sie zwei weitere Sachaufgaben zur Prozentrechnung mit mindestens zwei Lösungsschritten.
''')

# Begründen
st.header('2. Begründen – Umrechnung von Brüchen in Dezimalzahlen')

st.markdown('''
**Frage:** Warum funktioniert die Umrechnung von Brüchen in Dezimalzahlen?
''')

if st.checkbox('Begründung anzeigen'):
    st.info('Weil Brüche und Dezimalzahlen verschiedene Darstellungen desselben mathematischen Sachverhalts sind. Der Bruch stellt eine Division dar, und die Dezimalzahl ist das Ergebnis dieser Division.')

st.markdown('''
**Aufgabe für Sie:**

- Erklären Sie Ihren Schülerinnen und Schülern in einfachen Worten, warum der Bruch \(1/4) als Dezimalzahl 0,25 geschrieben werden kann. Geben Sie dabei auch ein anschauliches Beispiel aus dem Alltag (z.B. das Teilen einer Pizza in vier Stücke).
''')

# Modellieren
st.header('3. Modellieren – Handytarife vergleichen')

st.markdown('''
Ein Handytarif kostet monatlich 10 Euro Grundgebühr und zusätzlich 0,05 Euro pro Minute Telefonieren.

**Aufgabe:** Erstellen Sie ein mathematisches Modell, um die Gesamtkosten in Abhängigkeit von der Gesprächsdauer zu berechnen.
''')

minuten = st.slider('Telefonminuten auswählen:', 0, 500, 100)
gesamtkosten = 10 + minuten * 0.05
st.write(f'Gesamtkosten für {minuten} Minuten: {gesamtkosten:.2f} Euro')

st.markdown('''
**Aufgabe für Sie:** Entwickeln Sie eine ähnliche Modellierungsaufgabe zu einem anderen alltagsnahen Kontext, den Ihre Schülerinnen und Schüler aus ihrer Lebenswelt kennen.
''')

# Weitere Aufgaben für Referendare
st.header('Zusätzliche Aufgaben für Referendare')
st.markdown('''
- Entwickeln Sie weitere komplexe, alltagsnahe Sachaufgaben für Ihren Mathematikunterricht.
- Überlegen Sie, welche Herausforderungen Schülerinnen und Schüler beim Begründen und Modellieren haben könnten, und wie Sie sie gezielt unterstützen könnten.
- Gestalten Sie eine Unterrichtsstunde, in der Sie operative Durcharbeitung und kognitive Aktivierung effektiv umsetzen.
''')

