from scapy.all import IP, TCP, send  
from random import ranint
ip = IP(dst="109.176.239.69")
tcp = TCP(sport=randint(2000,60000), dport=443, flags="S") 

for i in range(10):
  send(ip/tcp)
print("finish")
