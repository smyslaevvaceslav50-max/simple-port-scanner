import socket
from datetime import datetime
import json
d = {}
ports = ["21", "22", "53", "80", "443"]
addres = input()
for i in ports:
    s = socket.socket()
    s.settimeout(2.0)
    t1 = datetime.now()
    if s.connect_ex((addres, int(i))) == 0:
        d[i] = f"Порт открыт; Секунд заняло: {(datetime.now() - t1).total_seconds()}"
    else:
        d[i] = f"Порт закрыт; Секунд заняло: {(datetime.now() - t1).total_seconds()}"
    s.close()

with open(r"I:\infa_ports.json", "w", encoding="utf-8") as file:
    json.dump(d, file)
print("write")
while True:
    work = input()
    if work == "close":
        break
    elif work == "open":
        with open(r"I:\infa_ports.json", encoding="utf-8") as file:
            fil = json.load(file)
            while True:
                print("What is port?")
                port = input()
                if port == "close":
                    break
                elif port in ports:
                    print(fil[port])
                else:
                    print("wrong port")
    else:
        print("wrong command")
