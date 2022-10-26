import cv2
import serial
import time
from gtts import gTTS
from playsound import playsound
from os import remove

def video():
    while cap.isOpened():
        ret, im = cap.read()
        try: 
            cv2.imshow('imagen',im)
        except:
            False
        if ret == False:
            break
        if cv2.waitKey(1) == 27:
            break
        time.sleep(0.04)
try: 
    serialArduino = serial.Serial("COM3",9600)
except:
    print('No se detecta el RUDE')

while True:

    cad = serialArduino.readline().decode('ascii')
    speech = gTTS(text = cad + 'centímetros', lang='es-us')
    speech.save('audio.mp3')
    print(cad)
    if int(cad) < 400:
        cad = int(cad)
        print(str(cad) + " centímetros")
        playsound('audio.mp3')
        while cad > 100:
            cap = cv2.VideoCapture('C:\\Users\\loque\\Documents\\GitHub\\proyecto\\videos\\num100.mp4')
            video()
            cad -= 100

        if cad <= 100:
            cap = cv2.VideoCapture('C:\\Users\\loque\\Documents\\GitHub\\proyecto\\videos\\num' + str(cad) + '.mp4')
            video()
        cap = cv2.VideoCapture('C:\\Users\\loque\\Documents\\GitHub\\proyecto\\videos\\cm.mp4')
        video()
    else:
        print('El RUDE no pudo detectar una superficie')
    try:
        remove("audio.mp3")
    except:
        print('No hay conexion a Internet')