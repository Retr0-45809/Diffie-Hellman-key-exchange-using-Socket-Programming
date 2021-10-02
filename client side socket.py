import socket
c = socket.socket()        
port = 9999             
c.connect(('localhost', port))
n=int(input("Enter n:"))
g=int(input("Enter g:"))
x=int(input("Enter x:"))
y=int(input("Enter y:"))
A=int(g^x%n)
K2=int(A^y%n)
print("Generated key for client is:",K2)
print (c.recv(1024).decode())
c.close()
