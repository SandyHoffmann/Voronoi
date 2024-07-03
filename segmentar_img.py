import cv2
import matplotlib.pyplot as plt
import numpy as np
# para segmentar imagem e exibir no diagrama de voronoi
def segmentar_imagem(image, max_points):
    imagem_binaria = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    # borrando imagens para gerar menos pontos
    imagem_borrada = cv2.medianBlur(imagem_binaria, 5)
    # canny ajuda a gerar as curvas da imagem
    edged = cv2.Canny(imagem_borrada, 30, 200)
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
    
    print("Numero de contornos = " + str(len(contours))) 

    keypoints = []

    max_points = max_points
    dimensao = 256
    
    # transformando os contornos em pontos
    # o max points define o range de contornos que irá ser exibido no voronoi
    for contorno in contours:
        n = contorno.ravel()
        i = 0
        espacamento = len(n) // max_points
        if espacamento == 0:
            espacamento = 1
        for ponto in n:
            if((i % espacamento) == 0 and i % 2 == 0):
                x = abs(dimensao - n[i])
                y = abs(dimensao - n[i + 1])
                keypoints.append([x, y])
            i = i + 1

    keypoints_to_values =keypoints
    keypoints_to_values.reverse()
    print("keypoints_to_values:", keypoints_to_values)
    print("keypoints_to_values:", len(keypoints_to_values))

    return keypoints_to_values