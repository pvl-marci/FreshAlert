import serial
import requests
import time

# Seriellen Port öffnen (angepasst an den COM-Port, an dem der Arduino angeschlossen ist)
ser = serial.Serial('COM6', 115200, timeout=1)
time.sleep(2)  # Warten, bis die Verbindung stabil ist

# HTTP-Anfrage an Telegram senden


def send_to_telegram(message):
    bot_token = '6961246644:AAHtc_YhctQmPUKe2z7-zdPDN93CvjLX0lo'
    bot_chatID = '-4111871844'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={message}'

    response = requests.get(send_text)
    return response.json()


# Haupt-Loop
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
            