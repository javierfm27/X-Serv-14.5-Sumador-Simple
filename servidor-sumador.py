#!/usr/bin/python3
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1231))
mySocket.listen(5)
operando1 = ''
operando2 = ''
try:
    while True:
        print("Waiting conections")
        (recvSocket,address) = mySocket.accept()
        print("Request received")
        peticion = recvSocket.recv(2048).decode('utf-8','strict')
        if(operando1 == ''):
            operando1 = peticion.split()[1][1:]
            recvSocket.send(bytes("HTTP/1.1 200 ok \r\n\r\n" +
                                "<!DOCTYPE html><html><body>" +
                                "Introduzca un operando" +
                                "</body> </html>","utf-8"))
        elif(operando1 != '' and operando2 == ''):
            operando2 = peticion.split()[1][1:]
            
        recvSocket.close()
except KeyboardInterrupt:
    print("Cerrando socket")
    mySocket.close()
