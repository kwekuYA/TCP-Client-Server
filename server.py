#import relevant modules
import socket

#define Server Address
host = socket.gethostname()

# specify port to listen on 
port = 9337

#create socket object and bind host and port
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.bind((host,port))

#Listen for incoming connections
sock_.listen(1)

print("\n Server has started...")

#accept conections
conn,addr = sock_.accept()

print(" Connection established with :" ,str(addr))

message = "\n Thank you for connecting " + str(addr)

#send messsage to client
conn.send(message.encode("ascii"))

#close connection
conn.close()

