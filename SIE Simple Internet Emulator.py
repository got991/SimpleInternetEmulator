# Simple Internet Emulator

import random
import time
import os

dev_mode = False

class Emulator(object):
    def __init__(self):
        self.hosts = []
        self.hostStatus = []
        self.requests = []
        self.responses = []
        self.delay = 0
        self.isTrueType = True
        self.isNumLegal = True
        self.isLengthLegal = True
        self.isLegal = True

    def verifyHostid(self, hostid):
        self.isTrueType = isinstance(hostid, str)
        self.isNumLegal = True
        self.isLengthLegal = len(hostid.split(":")) == 6
        if self.isTrueType and self.isLengthLegal:
            for i in hostid.split(":"):
                if (int(i, base=16)) > 255:
                    self.isNumLegal = False
                    break
        else:
            self.isNumLegal = False
        self.isLegal = self.isTrueType and self.isNumLegal and self.isLengthLegal
        return self.isLegal

    def createHost(self, name, open_port, hostid):
        if hostid is not None:
            if self.verifyHostid(self, hostid):
                self.hosts.append({'name': name, 'hostid': hostid, 'open_port': open_port})
                self.hostStatus.append({'hostid': hostid, 'status': 'closed', 'perm': {'full_access': True, 'read_access': True, 'write_access': True, 'execute_access': True, 'delete_access': True, 'configure_access': True, 'make_connection_access': True}, 'perm_status': 'closed', 'connections': {}})
                return hostid
            else:
                a = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                b = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                c = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                d = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                e = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                f = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
                hostidas = f'{a}:{b}:{c}:{d}:{e}:{f}'
                self.hosts.append({'name': name, 'hostid': hostidas,'open_port': open_port})
                self.hostStatus.append({'hostid': hostidas, 'status': 'closed', 'perm': {'full_access': True, 'read_access': True, 'write_access': True, 'execute_access': True, 'delete_access': True, 'configure_access': True, 'make_connection_access': True}, 'perm_status': 'closed', 'connections': {}})
                return hostidas
        else:
            a = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            b = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            c = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            d = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            e = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            f = str(hex(round(random.randint(0, 255)))).split('0x')[-1]
            hostidas = f'{a}:{b}:{c}:{d}:{e}:{f}'
            print(hostidas)
            self.hosts.append({'name':name, 'hostid': hostidas,'open_port': open_port})
            self.hostStatus.append({'hostid': hostidas, 'status': 'closed', 'perm': {'full_access': True, 'read_access': True, 'write_access': True, 'execute_access': True, 'delete_access': True, 'configure_access': True, 'make_connection_access': True}, 'perm_status': 'closed', 'connections': {}})
            return hostidas
        
    def gotoHost(self, hostid):
        print()

Emulator.hosts = []
Emulator.requests = []
Emulator.responses = []

def menu():
    if dev_mode == False:
        non_dev_menu()
    elif dev_mode == True:
        print(f"""
SIE Simple Internet Emulator Indev 0.0.1
(Devloper Mode Enabled)

Main Menu
1. Create New Host
2. Goto Host
3. Set Connection
4. Configure Hosts
5. Options
6. Exit

D: Close Devloper Mode
""")

def non_dev_menu():
    print(f"""
SIE Simple Internet Emulator Indev 0.0.1

Main Menu
1. Create New Host
2. Goto Host
3. Set Connection
4. Configure Hosts
5. Options
6. Exit

D: Open Devloper Mode(Requires Password)
""")
    select = input("> ")
    if select == "1":
        print("Create New Host")
        new_host_name = input("Name > ")
        new_host_opened_port = input("Opened Port (Like this: \"80.9999.25565.8888\") > ")
        formated_open_port = new_host_opened_port.split(".")
        new_host_id = input("HostID (* Not Required) > ")
        created_host_id = Emulator.createHost(Emulator, new_host_name, formated_open_port, new_host_id)
        print("This is HostID: " + created_host_id)
        menu()
    elif select == "2":
        print("Select Host")
        if len(Emulator.hosts) != 0:
            print("Hosts:")
            for host in Emulator.hosts:
                print(f"{host['name']} ({host['hostid']})")
            select_host = input("Enter HostID > ")
            if Emulator.verifyHostid(Emulator, select_host):
                Emulator.gotoHost(Emulator, select_host)
            else:
                print("Error: Wrong HostID, Back to the menu...")
                menu()
    elif select == "3":
        print("Set Connection")
        if len(Emulator.hosts) != 0:
            print("Hosts:")
            for host in Emulator.hosts:
                print(f"{host['name']} ({host['hostid']})")
            select_host = input("Enter Host 1's HostID > ")
            select_host2 = input("Enter Host 2's HostID > ")
            if Emulator.verifyHostid(Emulator, select_host) and Emulator.verifyHostid(Emulator, select_host2):
                Emulator.setConnection(Emulator, select_host, select_host2)
                print("Done.")
                menu()
            else:
                print("Not correct HostID. Back to the Menu...")
                menu()

        else:
            print("Oops, There is no host!")
            print("1. Menu")
            select = input("> ")
            if select == "1":
                menu()
            else:
                print("Not correct code. Back to the Menu...")
                menu()
    else:
        print("Not correct code. Please try again!")
        menu()

menu()