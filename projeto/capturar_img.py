import cv2

#Captura a webcam
video = cv2.VideoCapture(0)

#verifica se a conexão foi bem sucedida
if video.isOpened():
    #print("Conectou")
    validacao, frame = video.read()
    #loop infinito
    while validacao:
        validacao, frame = video.read()
        cv2.imshow("WebCam", frame)
        #Para a imagem por 5 ms e informa a interação do usuário no teclado
        #Obs.: Registra o número da tecla
        tecla = cv2.waitKey(5)

        #27 = tecla esc
        if (tecla == 27):
            break
    #Salva a img do ultimo frame
    cv2.imwrite("projeto/foto/Foto.png", frame)

#Finalizar a conexão com webcom
video.release()
#A img vai ser fechada
cv2.destroyAllWindows()