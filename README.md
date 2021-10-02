# Diffie-Hellman-key-exchange-using-Socket-Programming

The Diffie-Hellman algorithm is being used to establish a shared secret that can be used for secret communications while exchanging data over a public network using the elliptic curve to generate points and get the secret key using the parameters. For this we will be using Socket programming which is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. 

Algorithm:<br />
n and g are two large prime numbers<br />
A = g^x mod n where x is private key of sender<br />
B = g^y mod n where y is private key of client<br />
K1 = B^x mod n<br />
K2 = A^y mod n<br />
Hence K1 = k2<br />
