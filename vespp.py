'''
    File name: vespp.py
    Author: Dominic Anselmo
    Date created: 1/28/2022
    Description: A very simple Python proxy. Run it with Python, and answer the questions it asks at runtime.
'''
from socket import socket

def proxy_active():
    while 1:
        received = client.recv(1024)
        if not received: break
        proxy_client.sendall(received)

try:
    #We enclose the main logic in a try/except block because if we don't and the program crashes,
    #The listen port may remain open until the operating system eventually closes it.
    #There's no real harm in the port remaining open, but on some systems you'll have to 
    #wait for the OS to relinquish the port before you can run the program on the same port again.
    server = input("Enter the IP address of the remote server: ")
    listen_port = int(input("Enter the listening port to use: "))
    #If you get "Permission Denied" error after entering the port, 
    #your listening port is too low. Try a higher value.
    remote_port = int(input("Enter the remote port to use: "))

    proxy = socket()
    proxy.bind(("0.0.0.0",listen_port))
    proxy.listen(1)
    proxy_client = socket()
    
    print("Waiting for a connection...")
    client, addr = proxy.accept()
    #Script locks here until it gets a connection.

    print("You're connected! Connecting to server...")
    proxy_client.connect((server, remote_port))
    print("Connection successful! Proxy has begun forwarding.")
    proxy_active()
        
    proxy.close()

except Exception as e:
    proxy.close()
    print(e)
    raise

