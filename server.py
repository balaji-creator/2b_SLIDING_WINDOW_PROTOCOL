import socket
s=socket.socket()
s.bind(('127.0.0.1',8000))
s.listen(5)
print("Server is listening on port 8000...")   

conn,addr=s.accept()
print("Connection from:",addr)

while True:
    frame=conn.recv(1024).decode()
    if not frame:
        break
    print("Received frame:",frame)
    ack_message="ACK for frame: "+frame
    conn.send(ack_message.encode()) 
conn.close()    
s.close()