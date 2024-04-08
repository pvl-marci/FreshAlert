# FreshAlert - TinyML-basierte Gemüseklassifizierung

## Überblick
Kurze Beschreibung des Projekts und seiner Hauptfunktionen. Erläutern Sie den Zweck von FreshAlert und wie es mit einem Arduino Microcontroller arbeitet, um Gemüse zu scannen, zu klassifizieren und die Haltbarkeit des Gemüses über eine Telegram-Nachricht mitzuteilen.

## Inhaltsverzeichnis
- [Überblick](#überblick)
- [Technologien](#technologien)
- [Hardwareanforderungen](#hardwareanforderungen)
- [Softwareanforderungen](#softwareanforderungen)
- [Einrichtung und Installation](#einrichtung-und-installation)
  - [Modelltraining mit Edge Impulse](#modelltraining-mit-edge-impulse)
  - [Modelltesting mit Edge Impulse](#modelltesting-mit-edge-impulse)
  - [Modelldeployment via Arduino IDE](#modelldeployment-via-arduino-ide)
- [Python-Script für Telegram-Nachrichten](#python-script-für-telegram-nachrichten)
- [Verbindung und Datenübertragung](#verbindung-und-datenübertragung)
- [Benutzung](#benutzung)
- [Lizenz](#lizenz)
- [Autoren und Beitragende](#autoren-und-beitragende)
- [Danksagungen](#danksagungen)

## Technologien
- Arduino BLE 33 Sense
- Edge Impulse
- Arduino IDE
- Python
- Telegram BotFather
- Telegram API

## Hardwareanforderungen


## Softwareanforderungen
- Edge Impulse Web Interface
- Arduino IDE
- Telegram
- Python
- Imports:
    ```python
  import serial
  import requests
  import time
    ```
  


## Einrichtung und Installation
Schritte zur Einrichtung der Hardware und Installation der erforderlichen Software und Bibliotheken.

### Modelltraining mit Edge Impulse
Kurze Beschreibung, wie das Modell mit Edge Impulse trainiert wurde.

### Modelltesting mit Edge Impulse
Erläuterung, wie das Modell mit Edge Impulse getestet wurde.

### Modelldeployment via Arduino IDE
Anleitung, wie das Modell auf den Arduino Microcontroller über die Arduino IDE deployt wurde.

## Python-Script für Telegram-Nachrichten
### Projektbeschreibung: Telegram-basierte Erinnerung für Haltbarkeit von Obst und Gemüse

#### Ziel:
Das Ziel des Projekts besteht darin, den Nutzern eines Mikrocontrollers eine Erinnerung zur Haltbarkeit von Obst und Gemüse zu bieten. Hierfür wird die Übermittlung von Haltbarkeitsinformationen über die Telegram-Plattform realisiert.

#### Umsetzung:
1. **Einrichtung des Telegram-Bots:**
   - Ein Telegram-Bot wird mithilfe von "BotFather" erstellt.
   - Der Bot wird einer gemeinsamen Telegram-Gruppe hinzugefügt, an der alle beteiligten Nutzer teilnehmen.
   - Mithilfe von "IDBot" wird die Gruppen-ID exportiert und zusammen mit dem Bottoken des Bots in das Skript integriert.

2. **Serielle Verbindung mit dem Mikrocontroller:**
   - Eine serielle Verbindung mit dem Mikrocontroller wird hergestellt und konfiguriert.
   - Verwendete Funktion: `serial.Serial()`
     - `COM6`: Port, an den das Gerät angeschlossen ist.
     - `115200`: Baudrate für die serielle Kommunikation.
     - `timeout=1`: Zeitlimit für das Lesen von Daten.
    ```python
    ser = serial.Serial('COM6', 115200, timeout=1)
    time.sleep(2) 
    ```
      

3. **Funktion zur Nachrichtenübermittlung an Telegram:**
   - Die Funktion `send_to_telegram(message)` wird erstellt, um Nachrichten an den Telegram-Bot zu senden.
   - Die Funktion akzeptiert eine Nachricht als Argument.
   - Platzhalter für den Bot-Token und die Chat-ID werden innerhalb der Funktion verwendet.
   - Eine HTTPS-Anfrage-URL wird zusammengesetzt, um die Nachricht über die Telegram-API zu senden.
   - Die Funktion gibt die Antwort der Telegram-API als JSON zurück.
  
    ```python
    def send_to_telegram(message):
    bot_token = 'PLACEHOLDER'
    bot_chatID = 'PLACEHOLDER'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={message}'

    response = requests.get(send_text)
    return response.json()
    ```

4. **Erkennung und Benachrichtigung:**
   - In einer Endlosschleife wird kontinuierlich der serielle Port auf eingehende Daten überwacht.
   - Bei vorhandenen Daten wird eine Zeile aus dem seriellen Port gelesen, dekodiert und überflüssige Leerzeichen oder Zeilenumbrüche entfernt.
   - Wenn bestimmte Schlüsselwörter in der empfangenen Nachricht erkannt werden, wird eine entsprechende Benachrichtigung mit Haltbarkeitsangabe erstellt und an Telegram gesendet.
   - Erkannte Frucht- oder Gemüsesorten werden in der Konsole bestätigt, und bei Bedarf wird eine Nachricht an Telegram gesendet.
     ```python
      while True:
        if ser.in_waiting > 0:
          text = ""
          line = ser.readline().decode('utf-8').rstrip()        
          print("Vom Arduino erhalten:", line )
          if "Highest Value Label: banana" in line:
            text = "Banane erkannt 🍌 Sie ist noch 5 Tage haltbar"
            print(" 'banana' wurde erkannt"+ "\n")
            send_to_telegram(text)
          elif "Highest Value Label: paprika" in line:
            text = "Paprika erkannt 🫑 Sie ist noch 5 Tage haltbar"
            print("'paprika' wurde erkannt"+ "\n")
            send_to_telegram(text)
          elif "Highest Value Label: random" in line:
            text = "Kein Produkt erkannt 🤷‍♂️"
            print("'random' wurde erkannt - keine Nachricht an Telegram gesendet"+ "\n")          
     ```

#### Hinweise:
- Der Code wartet derzeit auf die Klassifizierung des Mikrocontrollers und sendet basierend auf dem Ergebnis Nachrichten an den Telegram-Bot.
- Es wurden keine genauen Berechnungen zur Haltbarkeit einzelner Obst- oder Gemüsesorten durchgeführt, da es sich um die Entwicklung eines Prototypen handelt.
- Die Platzhalter für den Bot-Token und die Chat-ID müssen durch die entsprechenden Werte ersetzt werden.
- Die genannten Code-Snippets wurden ausgelassen, um Fehler zu vermeiden.





## Verbindung und Datenübertragung
Erklärung, wie die USB-Verbindung zwischen dem Arduino und dem PC für die Serialerkennung eingerichtet wird.

## Benutzung
Anleitung, wie das System end-to-end verwendet wird, von der Gemüseerkennung bis zum Erhalt der Telegram-Nachricht.

## Lizenz
Informationen zur Lizenzierung Ihres Projekts.

## Autoren und Beitragende
Erkennung für alle, die zum Projekt beigetragen haben.

## Danksagungen
Optional können Sie hier Danksagungen einfügen, z.B. an Personen oder Organisationen, die Ihr Projekt unterstützt haben.

