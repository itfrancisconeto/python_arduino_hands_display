import serial
import cv2
import mediapipe as mp

""" References: 
https://www.section.io/engineering-education/creating-a-finger-counter/#results
https://blog.eletrogate.com/como-conectar-o-arduino-com-o-python/ 
"""

class ArduinoLed(object):
    
    def __init__(self):
        pass

    def getHandNumberArduino(self)->any:
        gravar5 = True
        gravar4 = False
        gravar3 = False
        gravar2 = False
        gravar1 = False
        gravar0 = False
        gravarD = True
        
        upCountGlobal = -9
        upCountTmp = -9
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils
        fingerCoord = [(8,6),(12,10),(16,14),(20,18)]
        thumbCoord = (4,2)        
        while True:
            success, image = cap.read()
            RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(RGB_image)
            multiLandMarks = results.multi_hand_landmarks
            if multiLandMarks:
                handList = []
                for handLms in multiLandMarks:
                    mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                    for idx, lm in enumerate(handLms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        handList.append((cx, cy))
                for point in handList:
                    cv2.circle(image, point, 10, (0, 0, 255), cv2.FILLED)
                    upCount = 0
                    for coordinate in fingerCoord:
                        if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                            upCount += 1
                    if handList[thumbCoord[0]][0] > handList[thumbCoord[1]][0]:
                        upCount += 1                   
                    cv2.putText(image, str(upCount), (40, 140), cv2.FONT_HERSHEY_PLAIN, 12, (0, 0, 255), 12)
                    upCountTmp = upCount
            cv2.imshow('Arduino Hands Display', image)
            if cv2.waitKey(1) & 0xff==ord('q'):
                break

            if upCountTmp == 5 and gravar5 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('5'.encode())
                gravar5 = False
                gravar4 = True
                gravar3 = True
                gravar2 = True
                gravar1 = True
                gravar0 = True
                gravarD = True
                arduino.flush()
            elif upCountTmp == 4 and gravar4 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('4'.encode())
                gravar5 = True
                gravar4 = False
                gravar3 = True
                gravar2 = True
                gravar1 = True
                gravar0 = True
                gravarD = True
                arduino.flush()
            elif upCountTmp == 3 and gravar3 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('3'.encode())
                gravar5 = True
                gravar4 = True
                gravar3 = False
                gravar2 = True
                gravar1 = True
                gravar0 = True
                gravarD = True
                arduino.flush()
            elif upCountTmp == 2 and gravar2 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('2'.encode())
                gravar5 = True
                gravar4 = True
                gravar3 = True
                gravar2 = False
                gravar1 = True
                gravar0 = True
                gravarD = True
                arduino.flush()
            elif upCountTmp == 1 and gravar1 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('1'.encode())
                gravar5 = True
                gravar4 = True
                gravar3 = True
                gravar2 = True
                gravar1 = False
                gravar0 = True
                gravarD = True
                arduino.flush()
            elif upCountTmp == 0 and gravar0 == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('0'.encode())
                gravar5 = True
                gravar4 = True
                gravar3 = True
                gravar2 = True
                gravar1 = True
                gravar0 = False
                gravarD = True
                arduino.flush()
            elif upCountTmp != 5 and upCountTmp != 4 \
                and upCountTmp != 3 and upCountTmp != 2 \
                and upCountTmp != 1 and upCountTmp != 0 \
                and gravarD == True:
                arduino = serial.Serial('/dev/ttyACM0', 9600)
                arduino.write('d'.encode())
                gravar5 = True
                gravar4 = True
                gravar3 = True
                gravar2 = True
                gravar1 = True
                gravar0 = True
                gravarD = False
                arduino.flush()
   
        cap.release()
        cv2.destroyWindow('Arduino Hands Display')

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    arduinoLed = ArduinoLed()
    arduinoLed.getHandNumberArduino()