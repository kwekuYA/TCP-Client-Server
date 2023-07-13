# Import relevant modules
import socket

#Create socket object
sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
sock_.connect((socket.gethostname(), 9337))

# receive message server sends
message = sock_.recv(1024)

#print message
print(message.decode("ascii"))