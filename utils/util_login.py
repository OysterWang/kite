#/usr/bin/python
#-*- coding:utf-8 -*-

import getpass
import telnetlib

HOST = "192.168.48.10"

tn = telnetlib.Telnet(HOST)
#tn.read_until(b"Password:")
tn.write(b"uxin@yxp@888\n")
tn.write(b"sh ip int b\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
tn.write(b"\n")
tn.write(b"exit\n")
#print(tn.read_until(b"36F-2960-48.10").decode('ascii'))
print(tn.read_all().decode('ascii'))
