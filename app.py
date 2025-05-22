
from flask import Flask, render_template, jsonify
import requests
import time
import threading
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Zugangsdaten und Konfiguration
USERNAME = "AKBSolar1"
PASSWORD = "DEIN_PASSWORT"  # Muss manuell ersetzt werden
SN = "BZP4NXM001"
LOGIN_URL = "https://server.growatt.com/login"
DATA_URL = "https://server.growatt.com/newEnergyAPI.do?action=getInvTodayData"

data_cache = {}

# Login-Funktion zur Token-Erstellung
def login():
    response = requests.post(LOGIN_URL, data={"userName": USERNAME, "password": PASSWORD})
    cookies = response.cookies.get_dict()
    return cookies

# Daten vom Growatt-Server abrufen
def fetch_data():
    global data_cache
    try:
        cookies = login()
        response = requests.post(DATA_URL, data={"invSn": SN}, cookies=cookies)
        result = response.json()
        data_cache = result.get("data", {})
    except Exception as e:
        print("Fehler beim Datenabruf:", e)

# Regelmäßiger Abruf im Hintergrund
def scheduler():
    while True:
        fetch_data()
        time.sleep(300)  # 5 Minuten

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify(data_cache)

if __name__ == "__main__":
    threading.Thread(target=scheduler, daemon=True).start()
    app.run(debug=True, port=5000)
