import socket,datetime
from random import randint


def main():

    host = "127.0.0.1"
    port = 12000

    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.bind((host,port))

    socketServer.listen(1)

    serverSocket,adr = socketServer.accept()
    print("Klienti eshte lidhur: " + str(adr))
    
    def ipaddr():
        return str(socket.gethostbyname(socket.gethostname()))

    def portnr():
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind(('', 0))
        addr, port = tcp.getsockname()
        tcp.close()
        return port 

    def Zanore(teksti):
        numratori=0
        for letter in teksti:
            if letter in "aeiouyAEIOUY":
                numratori+=1
        return numratori
    
    def printo(fjalia):
        return str(fjalia)

    def host():  
        return socket.gethostname()
        
    
    def fibonacci(number):
        if number==0: 
            return 0
        elif number==1: 
            return 1
        else : 
            return fibonacci(number-1)+fibonacci(number-2)

    def cift_tek(numri):
        if(numri%2==0):
            return "Numri "+ str(numri) +" eshte cift"
        else:
            return "Numri "+ str(numri) +" eshte tek"


    def time():
            date=datetime.datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")
            return date

    def loja():
        nr = ''
        for x in range(20):
            nr += str(randint(1,99))+ ' '
        return nr

    while True:
        mesazhi = serverSocket.recv(128).decode()
        if not mesazhi:
            break
        print("Mesazhi i pranuar eshte:"+ str(mesazhi))

        if mesazhi == "IPADDR":
            serverSocket.send(ipaddr().encode())

        elif mesazhi == "PORTNR":
            serverSocket.send(str(portnr()).encode('utf-8'))

        elif mesazhi == "ZANORE":
            mesazhi1=serverSocket.recv(128).decode()
            MesazhiDerguar=Zanore(mesazhi1)                
            serverSocket.send(str(MesazhiDerguar).encode())

        elif mesazhi == "PRINTO":
            printo1 = serverSocket.recv(128).decode()
            serverSocket.send(printo(printo1).encode())

        elif mesazhi == "HOST":
            serverSocket.send(str(host()).encode())

        elif mesazhi == "TIME":
            serverSocket.send(time().encode())

        elif mesazhi == "FIBONACCI":
            numri = serverSocket.recv(128).decode()
            serverSocket.send(str(int(fibonacci(int(numri)))).encode())

        elif mesazhi == "LOJA":
            serverSocket.send(loja().encode())

        elif mesazhi == "CIFT_TEK":
            numri = serverSocket.recv(128).decode()
            serverSocket.send(cift_tek(int(numri)).encode())


    serverSocket.close()

if __name__ == "__main__":
    main()