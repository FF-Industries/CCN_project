import socket
import struct
import time

# Function for Network Ping Tool
def network_ping(target_ip):
    try:
        # Create a raw socket using ICMP protocol
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        
        # Prepare the ICMP packet (Echo Request)
        icmp_type = 8  # ICMP Echo Request
        icmp_code = 0
        icmp_checksum = 0
        icmp_identifier = 1234  # You can choose any identifier
        icmp_sequence = 1  # Sequence number
        
        # Calculate ICMP checksum
        icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, icmp_identifier, icmp_sequence)
        icmp_checksum = 0
        for i in range(0, len(icmp_header), 2):
            icmp_checksum += (icmp_header[i] << 8) + icmp_header[i + 1]
        icmp_checksum = (icmp_checksum >> 16) + (icmp_checksum & 0xFFFF)
        icmp_checksum = ~icmp_checksum & 0xFFFF
        
        # Update the ICMP header with the calculated checksum
        icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, socket.htons(icmp_checksum), icmp_identifier, icmp_sequence)
        
        # Send the ICMP packet to the target IP
        icmp_packet = icmp_header
        icmp_socket.sendto(icmp_packet, (target_ip, 0))
        
        # Receive ICMP Echo Reply
        icmp_socket.settimeout(10)  # Timeout in seconds
        start_time = time.time()
        response, addr = icmp_socket.recvfrom(1024)
        end_time = time.time()
        
        # Calculate Round Trip Time (RTT)
        rtt = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f'Reply from {target_ip}: time={rtt:.2f}ms')
        
    except socket.error as e:
        print(f'Ping to {target_ip} failed: {e}')

    finally:
        icmp_socket.close()

# Function for Port Scanner Tool
def port_scanner(target_ip, start_port, end_port):
    print(f'Scanning ports on {target_ip}...')
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout for the connection attempt
            client_socket.settimeout(1)
            
            # Attempt to connect to the target IP and port
            result = client_socket.connect_ex((target_ip, port))
            
            if result == 0:
                open_ports.append(port)
                print(f'Port {port} is open')
            
            # Close the socket
            client_socket.close()
        
        except KeyboardInterrupt:
            print('\nPort scanning aborted by user.')
            return
        
        except socket.error:
            pass  # Port is closed or unreachable

    if open_ports:
        print('Open ports:', open_ports)
    else:
        print('No open ports found.')

if __name__ == "__main__":
    try:
        target_ip = input("Enter the target IP address: ")
        
        # Task 1: Network Ping Tool
        network_ping(target_ip)
        
        # Task 2: Port Scanner Tool
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
        
        port_scanner(target_ip, start_port, end_port)
    
    except ValueError:
        print("Invalid input. Please enter a valid IP address and port numbers.")
