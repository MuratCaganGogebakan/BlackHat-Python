import socket
import os

# Host to listen on
HOST = "192.168.1.38"

def main():
    # Create raw socket, bin to public interface
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST,0))
    # Include the IP Header in the Capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == "nt":
        sniffer.iotctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    # Read one packet
    print(sniffer.recvfrom(65565))

    # if we are on Windows turn off promiscious mode
    if os.name == "nt":
        sniffer.iotctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    print("starting")
    main()

