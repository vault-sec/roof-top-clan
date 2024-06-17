#!/usr/bin/python3

import getpass
import telnetlib

host = "my-server.example.net"
user = "admin"
password = "letmein321"

tn = telnetlib.Telnet(host)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
