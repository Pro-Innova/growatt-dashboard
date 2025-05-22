
# Growatt Dashboard (ShinePhone API)

Ein einfaches Web-Dashboard zur Visualisierung von Growatt PV-Daten (z. B. ShinePhone oder ShineServer).

## Funktionen

- Abfrage der Wechselrichterdaten (z. B. Tagesleistung)
- Darstellung als Liniendiagramm im Browser
- Automatische Aktualisierung alle 5 Minuten

## Voraussetzungen

- Python 3.x
- Pakete: `flask`, `requests`

## Installation

```bash
pip install flask requests
python app.py
```

Dann im Browser öffnen: [http://localhost:5000](http://localhost:5000)

## Konfiguration

Trage dein Growatt-Passwort in `app.py` ein:

```python
PASSWORD = "HIER_DEIN_PASSWORT"
```

## Lizenz

MIT License
