# packert
packert is a multithreaded python packet generation tool

#Packert

Packert is a Python program that generates random packets and sends them to a specified server. The program allows the user to specify the number of threads to use, the number of packets per thread, and the delay between packets.

Requirements
Python 3.x
socket module
struct module
random module
threading module
time module
Usage

To use Packert, run the following command:


python packert.py


You will be prompted to enter the following information:

Target server's IP address
Target server's port number
Number of threads to use
Number of packets per thread
Minimum delay between packets (in seconds)
Maximum delay between packets (in seconds)

Once you have entered all the required information, Packert will start generating and sending packets to the specified server.

# How it works

The send_packets() function generates random packets and sends them to the specified server. The function takes six arguments:

target_ip: The IP address of the target server.
target_port: The port number of the target server.
num_threads: The number of threads to use.
num_packets_per_thread: The number of packets to send per thread.
min_delay: The minimum delay between packets (in seconds).
max_delay: The maximum delay between packets (in seconds).

The function first creates a new socket and connects to the server. It then generates and sends packets based on the specified parameters. For each packet, the function generates a random payload, protocol, source IP address, and source port. It then constructs the packet header and IP packet, and sends the packet to the server.

The menu() function prompts the user to enter the required information and starts the packet generation process by creating a new thread for each specified thread. The function then waits for all the threads to finish before terminating.

# Notes
Packert uses raw sockets to generate and send packets, which requires root privileges on most systems.
Packert is intended for educational and testing purposes only. Do not use this program to perform any illegal or malicious activities.
