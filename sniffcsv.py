import csv
import scapy.all as scapy
import sys

if len(sys.argv) != 2:
    print("rong input ")
    exit()
lon = sys.argv[1]

def sniff_dns(packet):
  q=[1]
  if packet.haslayer(scapy.DNS) :
    q.append(packet[scapy.IP].src)
    print("Source IP address:", packet[scapy.IP].src)
    q.append(packet[scapy.IP].src)
    print("Destination IP address:", packet[scapy.IP].dst)
    q.append(packet[scapy.IP].dst)
    print("Protocol:", packet[scapy.IP].proto)
    q.append(packet[scapy.IP].proto)

    
    print("DNS query for:", packet[scapy.DNS].qd.qname)
    q.append(packet[scapy.DNS].qd.qname)
    
    print("Question type:", packet[scapy.DNS].qd.qtype)
    q.append(packet[scapy.DNS].qd.qtype)
    print("Question class:", packet[scapy.DNS].qd.qclass)
    q.append(packet[scapy.DNS].qd.qclass)
    print(packet[scapy.DNS].id)
    q.append(packet[scapy.DNS].id)
    print(packet[scapy.DNS].qr)
    q.append(packet[scapy.DNS].qr)
    print(packet[scapy.DNS].opcode)
    q.append(packet[scapy.DNS].opcode)
    print(packet[scapy.DNS].rd)
    q.append(packet[scapy.DNS].rd)
    print(packet[scapy.DNS].qdcount)
    q.append(packet[scapy.DNS].qdcount)
    with open(lon, "a") as f:
      writer = csv.writer(f)
      writer.writerow(q)
