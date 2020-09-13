import cv2 #Importamoos la libreria opencv
import numpy as np #Importamoos la libreria numpy

video = cv2.VideoCapture("Juguete.mp4")

i = 0 #Iniciamos un contador. Servirá para captar el fondo de la imagen.
while True: #Leemos las imagenes del video que se almacenarán en frame, y en caso de que no se haya podido tomar una imagen se rompe el ciclo while.
  ret, frame = video.read()
  if ret == False: break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Para tranasformar de BGR a escala de grises unsamos la función cvcv2.cvtColor.
  if i == 20: #Cuando el contador llega a 20, entonces se graba la imagen gray en bgGray, que será la imagen del fondo de la escena. Esta nos servirá para restarla de la imagen actual.
    bgGray = gray
  if i > 20: #Una vez que el contador es mayor a 20, se procede a usar cv2.absdiff, para poder restar la imagen actual y la del fondo
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    # Para OpenCV 3
    #_, cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Para OpenCV 4
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    for c in cnts: # Analizaremos cada contorno dentro de cnts
      area = cv2.contourArea(c) #Se emplea la función cv2.contourArea, para determinar el área en pixeles del contorno
      if area > 9000: #Si el área es mayor a 9000, entonces se aplica cv2.boundingRect que devuelve las coordenadas x e y, a más del ancho y alto del contorno. Luego para dibujar este contorno usaremos la información de la línea 25 y dibujaremos un rectángulo con cv2.rectangle.
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

  cv2.imshow('Frame',frame) #Visualizamos el proceso realizado en frame.

  i = i+1 # Aumentamos en 1 el contador.
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()