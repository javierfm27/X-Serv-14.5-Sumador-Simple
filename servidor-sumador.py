#!/usr/bin/python3
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1232))
mySocket.listen(5)
state = 0

try:
    while True:
        print("Waiting conections")
        (recvSocket,address) = mySocket.accept()
        print("Request received")
        peticion = recvSocket.recv(2048).decode('utf-8','strict')
        print(peticion)
        peticion = peticion.split()
        if state == 0:
            state = 1
            operando1 = peticion[1][1:]
            recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" +
                                "<!DOCTYPE html> <html><body>" +
                                "<h5>El primer operando es  " +
                                str(operando1) +
                                ", introduzca el segundo operando" +
                                "</h5>" +
                                "</body></html>\r\n","utf-8"))
        else:
            operando2 = peticion[1][1:]
            resultado = int(operando1) + int(operando2)
            recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" +
                                "<!DOCTYPE html><html><body>" +
                                "<h4> El resultado de sumar " +
                                operando1 +
                                " y " +
                                operando2 +
                                " es " +
                                str(resultado) +
                                "</h4></body></html>\r\n","utf-8"))
            state = 0
        recvSocket.close()
except KeyboardInterrupt:
    print("Cerrando socket")
    mySocket.close()
