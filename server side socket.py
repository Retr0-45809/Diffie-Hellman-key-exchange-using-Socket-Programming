import socket            
s = socket.socket()        
print ("Socket successfully created")
port = 9999               
s.bind(('localhost', port))        
print ("socket binded to %s" %(port))
s.listen(3)
n=int(input("Enter n:"))
g=int(input("Enter g:"))
x=int(input("Enter x:"))
y=int(input("Enter y:"))
B=int(g^y%n)
K1=int(B^x%n)
print("Generated key for server is:",K1)    
print ("Waiting for connection")           
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send('Thank you for connecting'.encode())
  c.close()
  break