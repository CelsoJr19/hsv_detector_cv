import cv2
import numpy as np
import serial
import time

cap = cv2.VideoCapture(0) #Abre a webcam

arduino = serial.Serial('COM3', 9600) #Configura a comunicação serial com o Arduino
time.sleep(2) #Aguarda a conexão ser estabelecida

while True:
   
    ret, frame = cap.read() #Lê o frame da câmera
    cor_detectada = False
    if not ret:
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converte o frame de BGR para HSV

    """
    #Define o range da cor vermelha no espaço HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([2, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_red, upper_red)"""

     
    #Define o range da cor laranja no espaço HSV
    lower_orange = np.array([4, 100, 100])
    upper_orange = np.array([19, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    """
    #Define o range da cor amarela no espaço HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)"""

    """
    #Define o range da cor verde no espaço HSV
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_green, upper_green)"""

    """
    #Define o range da cor ciano no espaço HSV
    lower_cyan = np.array([87, 100, 100])
    upper_cyan = np.array([99, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_cyan, upper_cyan)"""

    """
    #Define o range da cor azul no espaço HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([129, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_blue, upper_blue)"""

    """
    #Define o range da cor roxa no espaço HSV
    lower_purple = np.array([130, 50, 40])
    upper_purple = np.array([142, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_purple, upper_purple)"""

    """
    #Define o range da cor rosa no espaço HSV
    lower_pink = np.array([142, 50, 40])
    upper_pink = np.array([170, 255, 255])

    #Cria a máscara
    mask = cv2.inRange(hsv, lower_pink, upper_pink)"""

    #Aplica a máscara na imagem original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #Encontra os contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    """
    #Desenha um retângulo ao redor do maior contorno vermelho encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Objeto Vermelho", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cor_detectada = True"""

    
    #Desenha um retângulo ao redor do maior contorno laranja encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2)
            cv2.putText(frame, "Objeto Laranja", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,165,255), 2)
            cor_detectada = True
    
    """
    #Desenha um retângulo ao redor do maior contorno amarelo encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Objeto Amarelo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
            cor_detectada = True"""
    
    """
    #Desenha um retângulo ao redor do maior contorno verde encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Objeto Verde", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            cor_detectada = True"""
    
    """ 
    #Desenha um retângulo ao redor do maior contorno ciano encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Objeto Ciano", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
            cor_detectada = True"""

    """
    #Desenha um retângulo ao redor do maior contorno azul encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Objeto Azul", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
            cor_detectada = True"""

    """
    #Desenha um retângulo ao redor do maior contorno roxo encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 10, 130), 2)
            cv2.putText(frame, "Objeto Roxo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)
            cor_detectada = True"""

    """
    #Desenha um retângulo ao redor do maior contorno rosa encontrado
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: #Ignora pequenos ruídos
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(frame, "Objeto Rosa", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)
            cor_detectada = True"""

    # Envia '1' se achou a cor, e '0' se não achou nada
    if cor_detectada:
        arduino.write(b'1')
    else:
        arduino.write(b'0')
        
    #Mostra os resultados na tela
    cv2.imshow('Camera Original', frame)
    cv2.imshow('Mascara', mask)

    #Aperte 'c', de Celso, para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
