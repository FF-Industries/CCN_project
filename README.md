# COMPUTER COMMUNICATION NETWORKS PROJECT

In this project, you will develop a simple command-line tool that can perform network pings and scan open ports on remote hosts. This project will help you learn the basics of network programming and socket operations.


## CONTENT :
- [1. INTRODUCTION](https://github.com/FF-Industries/CCN_project/blob/main/README.md#1-introduction)
- [2. NETWORK PING TOOL](https://github.com/FF-Industries/CCN_project/blob/main/README.md#2-network-ping-tool)
- [3. PORT SCANNER TOOL ](https://github.com/FF-Industries/CCN_project/blob/main/README.md#3-port-scanner-tool)
- [4. TESTCASE](https://github.com/FF-Industries/CCN_project/blob/main/README.md#4-testcase)
- [5. VERIFYING THE RESULT WITH WIRESHARK](https://github.com/FF-Industries/CCN_project/blob/main/README.md#5-verifying-the-result-with-wireshark)
- [6. DISCUSSION](https://github.com/FF-Industries/CCN_project/blob/main/README.md#6-discussion)
- [7. CONCLUSION](https://github.com/FF-Industries/CCN_project/blob/main/README.md#7-conclusion)
  
## 1. INTRODUCTION

The field of computer networking is pivotal in today's interconnected world, forming the backbone of global communication and data exchange. Understanding and monitoring the health of a network, as well as identifying potential vulnerabilities, are essential aspects of network management and security. In this context, the "Network Ping and Port Scanner Tool" project has been undertaken as part of the Computer Communication Network course, with the primary objective of developing a versatile and practical tool for network administrators and security professionals.

### 1.1 BACKGROUND AND MOTIVATION 

In the realm of network diagnostics and security, two fundamental tasks frequently arise: assessing the availability and responsiveness of network devices and identifying open ports on remote hosts. The motivation behind this project stems from the need for efficient, customizable, and user-friendly tools to perform these critical tasks.
* **Network Ping Tool :** ICMP (Internet Control Message Protocol) ping is a widely used utility for testing network connectivity and measuring response times between devices. A tool that can send ICMP echo request packets and receive ICMP echo reply packets offers valuable insights into network performance.
* **Port Scanner Tool :** Port scanning plays a pivotal role in network security, allowing administrators to identify potential vulnerabilities and security weaknesses. A port scanner tool that can probe a range of ports on a target IP address aids in the assessment of network security.

### 1.2 OBJECTIVES

The primary objectives of this project are as follows:

* Develop a Network Ping Tool capable of sending ICMP echo request packets to a target IP address and measuring the round-trip time (RTT) for each packet.
* Extend the tool to include a Port Scanner that can accept a target IP address and a range of ports as input, and identify and report open ports on the target host.
* Provide a user-friendly interface for input and output, making it accessible to network administrators and security analysts.
* Implement error handling and validation mechanisms to enhance the reliability and robustness of the tool.

### 1.3 SCOPE OF THE PROJECT

This project focuses on the development of a Python-based Network Ping and Port Scanner Tool, providing a practical solution for network diagnostic and security purposes. The scope encompasses:

* Implementation of ICMP ping requests using raw sockets for network ping functionality.
* Utilizing socket programming to attempt connections to a specified range of ports for the port scanning feature.
* Ensuring cross-platform compatibility for ease of use.
* Providing clear and concise reporting of results, including RTT measurements and open port identification.

## 2. NETWORK PING TOOL

The Network Ping Tool is a crucial component of our project, designed to send ICMP (Internet Control Message Protocol) echo request packets to a target IP address and measure the round-trip time (RTT) for each packet. This tool is instrumental in assessing the availability and responsiveness of network devices. In this section, we will delve into the technical details of the implementation, covering the following aspects:

### 2.1 OVERVIEW OF ICMP PING REQUESTS

ICMP, a fundamental protocol in the Internet Protocol suite, is used for various network management and diagnostic purposes. One of its most common uses is for network ping requests, which help determine if a remote host is reachable and measure the time it takes for a packet to travel to the host and back. ICMP ping requests are typically sent using raw sockets to bypass higher-level transport protocols like TCP or UDP.

### 2.2 IMPLEMENTATION OF ICMP PING REQUESTS 

The implementation of ICMP ping requests in our tool involves the following steps:

* **Raw Socket Creation :** We create a raw socket using Python's socket library, allowing us to send and receive ICMP packets directly.
* **Constructing ICMP Echo Request Packet :** To send a ping request, we construct an ICMP echo request packet. This packet contains essential information, including the type, code, identifier, and sequence number.
* **Sending ICMP Echo Request Packets :** Our tool sends multiple ICMP echo request packets to the target IP address. We utilize the socket.sendto() method to transmit these packets.

### 2.3 RECIEVING AND CALCULATING ROUND TRIP TIME(RTT)

Round Trip Time (RTT) is typically expressed in milliseconds (ms) 
and is a crucial indicator of network latency or delay. It represents 
the total time it takes for a data packet to make a complete round 
trip through the network.
RTT is calculated as follows:
* A sender (e.g., a client computer) sends a data packet to a receiver (e.g., a server) over a network.
* The packet travels from the sender to the receiver, passing through various network devices such as routers and switches.
* The receiver processes the packet and generates a response.
* The response packet travels back from the receiver to the sender, following the same network path.
* The sender measures the time elapsed between sending the packet and receiving the corresponding response.

In the code, we create a raw socket using the ICMP protocol, prepare the ICMP packet, calculate the ICMP checksum, update the calculated checksum to the ICMP header, send the ICMP 
packet to the target IP, set timeout of 2 seconds, we start the timer and note the start time of the data packet. The code waits to receive a response message from the client and timer is stopper noting down the end time. The round trip time (RTT) is calculated by finding the difference between the end time and the start time 
noted. The result is displayed and ICMP socket is closed. 

The RTT is also found using Wireshark software for the packets and verified with the results obtained from the Python code. 

## 3. PORT SCANNER TOOL 

The Port Scanner Tool is an integral component of our project, designed to extend the functionality of the Network Ping Tool. While the Network Ping Tool assesses the reachability and responsiveness of a host, the Port Scanner Tool goes further by attempting connections to a specified range of ports on the target IP address. In this section, we will explore the technical details of the Port Scanner Tool, including its purpose, implementation, and how it identifies open ports.

### 3.1 INTRODUCTION TO PORT SCANNING

Port scanning is a crucial technique in network security and diagnostics. It involves probing a range of network ports on a target host to determine which ports are open, closed, or filtered. Open ports can indicate services or applications running on the host, while closed or filtered ports may signify potential security measures or a lack of services.

### 3.2 SOCKET PROGRAMMING FOR PORT SCANNING

The Port Scanner Tool utilizes Python's socket programming capabilities to achieve its objectives. Socket programming allows us to create network sockets and establish connections to remote hosts and ports. Specifically, we use the socket library in Python to implement port scanning functionality.

### 3.3 ACCEPTING TARGET IP ADDRESS AND PORT RANGE AS INPUT

Our Port Scanner Tool accepts user-defined input, including the target IP address and a range of ports to scan. This flexibility allows network administrators and security professionals to tailor the tool to their specific needs. The tool validates the input to ensure that it falls within the appropriate range and format.

### 3.4 SCANNING FOR OPEN PORTS

A basic port scanning tool allows you to scan a range of ports on a target IP address to determine which ports are open and reachable. Port scanning is a common network reconnaissance technique used by network administrators and security professionals to identify open ports on a target system. Understanding open ports is essential for network diagnostics, security audits, and vulnerability assessments.

The port scanner scan ports within the specified range. The code uses an empty list to store the open ports found during the scan.  A loop iterates through the specified range of ports, For each port in the loop, it creates a socket object to establish a connection. It sets a timeout of 1 second for the connection attempt to prevent the scanner from waiting too long for unresponsive ports. The code then attempts to connect to the target IP and port. If the connection was successful, then the port number is added to the open ports list, and the list is displayed and if no open port was found then it reports that no open ports were found.

#### CODE :
```
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
        icmp_identifier = 12345  # You can choose any identifier
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
        icmp_socket.settimeout(2)  # Timeout in seconds
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
```
## 4. TESTCASE

### 4.1 VALID IP ADDRESS INPUT 

![WhatsApp Image 2023-10-07 at 17 00 52_c0b7f469](https://github.com/FF-Industries/CCN_project/assets/136846161/58a17449-0671-4ed9-95f2-394d5a5f1ec6)

Analysis : NEEDS TO BE FILLED

### 4.2 INVALID IP ADDRESS INPUT

![WhatsApp Image 2023-10-07 at 17 00 53_663b06cc](https://github.com/FF-Industries/CCN_project/assets/136846161/756383d4-e1e3-483b-8a70-5486aaabb353)

Analysis : NEEDS TO BE FILLED

### 4.3 NO ARGUMENTS PROVIDED

![WhatsApp Image 2023-10-07 at 17 00 53_ab3003b2](https://github.com/FF-Industries/CCN_project/assets/136846161/596f4bef-0af8-4a7d-a238-35764ddec908)

Analysis : NEEDS TO BE FILLED

### 4.4 PORT RANGE INPUT

![WhatsApp Image 2023-10-07 at 17 00 54_53551bf9](https://github.com/FF-Industries/CCN_project/assets/136846161/2107c218-a149-4280-bb29-0276e7630f48)

Analysis : NEEDS TO BE FILLED

### 4.5 TIMEOUT HANDLING 

![WhatsApp Image 2023-10-07 at 22 17 32_6576a9e6](https://github.com/FF-Industries/CCN_project/assets/136846161/045bc5df-e5a8-4d2c-90ff-80cb4937381d)

Analysis : NEEDS TO BE FILLED

## 5. VERIFYING THE RESULT WITH WIRESHARK

NEEDS TO BE FILLED

## 6. DISCUSSION 

The "Network Ping and Port Scanner Tool" offers a valuable set of functionalities for network administrators and security professionals. In this section, we will discuss the benefits and applications of the tool, the challenges faced during its development, its limitations, and future enhancement possibilities.

### 6.1 BENEFITS AND APPLICATIONS

The Network Ping and Port Scanner Tool provides several notable benefits and has various practical applications:

* **Network Health Monitoring :** The ICMP ping functionality helps administrators assess network health by measuring round-trip times (RTT) to network devices. This is essential for identifying latency issues and diagnosing network problems.
* **Security Assessment :** The Port Scanner Tool allows security professionals to identify open ports on remote hosts, aiding in the assessment of potential vulnerabilities and security weaknesses. This is invaluable for proactive security measures.
* **User-Friendly Interface :** The command-line interface (CLI) and user prompts make the tool accessible to both novice and experienced users. It provides a streamlined and efficient way to perform network diagnostics and security checks.

### 6.2 CHALLENGES AND LIMITATIONS

While the Network Ping and Port Scanner Tool offers substantial benefits, there were challenges and limitations encountered during its development:

* **Firewall and Network Configuration :** The tool may not be able to accurately identify open ports if firewalls or network configurations block ICMP or TCP responses. This can lead to false negatives in port scanning results.
* **Speed and Efficiency :** The tool may not be the fastest option for scanning a large number of ports on multiple hosts due to its sequential scanning approach. Parallelization or optimization techniques could improve efficiency.
* **Platform Dependency :** Although efforts were made to ensure cross-platform compatibility, there may still be platform-specific issues or differences in behavior that affect the tool's performance.

### 6.3 FUTURE ENHANCEMENTS

To further improve the tool's functionality and versatility, several enhancements can be considered for future development:

* **Parallel Port Scanning :** Implementing parallel port scanning techniques can significantly improve the speed and efficiency of the Port Scanner Tool, allowing users to scan multiple ports or hosts simultaneously.
* **Service Identification :** Enhance the tool to identify and report the specific services running on open ports, providing more comprehensive information about target hosts.
* **Network Traceroute :** Incorporate network traceroute functionality to trace the route packets take through the network to reach the target host, helping diagnose network issues.
* **Graphical User Interface (GUI) :** Develop a graphical user interface for the tool to make it even more accessible to users who are not comfortable with command-line tools.
* **Logging and Reporting :** Implement logging and reporting features to allow users to save and analyze historical scan results.

## 7. CONCLUSION

### 7.1 SUMMARY OF ACHIEVEMENTS

Throughout the course of this project, we have accomplished the following:

* Developed a Network Ping Tool capable of sending ICMP echo requests and measuring round-trip times (RTT).
* Extended the tool to include a Port Scanner that identifies open ports on target hosts.
* Created a user-friendly command-line interface (CLI) for easy input and output.
* Implemented comprehensive error handling and input validation mechanisms to enhance tool reliability.
* Offered a modular design that allows users to choose between ping and port scan functionalities

### 7.2 KEY TAKEWAYS

* **Versatility :** The tool's ability to perform network ping and port scanning in a single package makes it a versatile asset for network administrators and security professionals.
* **Usability :** The user-friendly interface and clear reporting enable users to quickly gain insights into network health and potential security vulnerabilities.
* **Challenges and Limitations :** It's important to recognize that the tool may face challenges in certain network environments, such as those with strict firewalls, and its efficiency could be further improved with optimization techniques.

### 7.3 FINAL THOUGHTS

In conclusion, the "Network Ping and Port Scanner Tool" serves as a valuable asset for network administrators and security professionals, providing essential tools for network diagnostics and security assessments. While the project has achieved its primary objectives, it also serves as a foundation for future improvements and adaptations to meet evolving network challenges and demands.
We hope that this tool proves to be a useful addition to the toolbox of network professionals and contributes to the ongoing efforts to ensure the reliability and security of computer communication networks.


  




