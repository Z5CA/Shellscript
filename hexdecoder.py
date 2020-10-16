#!/usr/bin/python3
import math
ip=input().strip()

ip=ip.replace('\\x',' ').strip()
ip=ip.replace('0x',' ').strip()
ip=ip.replace('%',' ').strip()

arr=ip.split(' ')
if len(arr)<math.ceil( len(ip)/3):
    ip=ip.replace(' ','').strip()
    ipn=[]
    for i in range(0,len(ip),2):
        ipn.append(ip[i:i+2])
    arr=ipn

print("Output:")
print()
for i in arr:
    print(chr(int(i,16)),end='')
print()