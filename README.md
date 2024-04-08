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
  - serial
  - requests
  - time
- 


## Einrichtung und Installation
Schritte zur Einrichtung der Hardware und Installation der erforderlichen Software und Bibliotheken.

### Modelltraining mit Edge Impulse
Kurze Beschreibung, wie das Modell mit Edge Impulse trainiert wurde.

### Modelltesting mit Edge Impulse
Erläuterung, wie das Modell mit Edge Impulse getestet wurde.

### Modelldeployment via Arduino IDE
Anleitung, wie das Modell auf den Arduino Microcontroller über die Arduino IDE deployt wurde.

## Python-Script für Telegram-Nachrichten
Ziel des Projekts war es, dass die Nutzenden des Mikrocontrollers eine Erinnerung zur Haltbarkeit des eingekauften Obsts/Gemüses erhalten. Dafür war in unserem Projekt die Übermittlung von Haltbarkeiten via Telegram vorgesehen. Aufgrund der Tatsache, dass es sich hierbei um die Entwicklung eines Prototypen handelt, wurden keine genauen Berechnungen zur Haltbarkeit einzelner Gemüse- bzw. Obstsorten vorgenommen. Das Skript wartet derzeit lediglich auf die Klassifizierung des Mikrocontrollers und verschickt auf Basis des Ergebnisses eine Nachricht an unseren Telegrambot via API.

Dazu wurde im ersten Schritt ein Telegram-Bot mit "BotFather" erstellt. Dieser wurde im Anschluss mit allen Beteiligten zu einer gemeinsamen Telegram-Gruppe hinzugefügt. Mittels eines des "IDBot" wurde die GruppenID exportiert und zusammen mit dem Bottoken des zuvor erstellen FreshAlert Bots in ein Skript implementiert.

```python
def hello_world():
print("Hello, world!")
```

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

