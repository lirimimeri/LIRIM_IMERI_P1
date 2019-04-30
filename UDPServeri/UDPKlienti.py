import socket

def main():

    host = "127.0.0.1"
    port = 12000

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host,port))

    mesazhi1 = ''
    while mesazhi1 != 'q':
        mesazhi1 = input("Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, NOTA, PERFUNDO)?   ")
        mesazhi = str(mesazhi1).upper()
        clientSocket.send(mesazhi.encode())
            
        if mesazhi == "IPADRESA":
            data = clientSocket.recv(128).decode()
            print("Ip adresa: " + str(data))

        elif mesazhi == "NUMRIIPORTIT":
            data = clientSocket.recv(128).decode('utf-8')
            print("Numri i portit: " + str(data))

        elif mesazhi == "ZANORE":
            mesazhi1=serverSocket.recv(128).decode()
            MesazhiDerguar=Zanore(mesazhi1)                
            serverSocket.send(str(MesazhiDerguar).encode())
        
        elif mesazhi == "PRINTO":
            printo1=input("Fjalia:")
            clientSocket.send(str(printo1).encode())
            printo2=clientSocket.recv(128)
            print("Fjalia e derguar: "+printo2.decode())
      
        elif mesazhi == "HOST":
            hosti = clientSocket.recv(128).decode()
            print("Emri i hostit: " +hosti)

        elif mesazhi == "KOHA":
            print(clientSocket.recv(128).decode())

        elif mesazhi == "FIBONACCI":
            numri = input("Numri: ")
            clientSocket.send(numri.encode())
            fibi = clientSocket.recv(128).decode()
            print("Rezultati: " + fibi)

        elif mesazhi == "LOJA":
            print("Numrat: " +clientSocket.recv(128).decode())

        elif mesazhi == "PERFUNDO":
            mesazhi1="q"

        elif mesazhi =="NUMERITHJESHTE":
            numri = input("Numri: ")
            clientSocket.send(numri.encode())
            rezultati = clientSocket.recv(128).decode()
            print(rezultati)



    clientSocket.close()

if __name__ == "__main__":
    main()