import socket
s=socket.socket()
s.connect(('127.0.0.1',8000))

size=int(input("Enter frame size: "))
l=list(range(size))
frame_size=int(input("Enter frame size to send: "))
i=0
while True:
    while i<len(l):
        st=i+frame_size
        frame_to_send=l[i:st]
        print("Sending frame:",frame_to_send)   
        s.send(str(frame_to_send).encode())
        ack=s.recv(1024).decode()
        if not ack:
            break
        else:
            print("Received acknowledgment:",ack)
        i+=frame_size
    break
s.close()
