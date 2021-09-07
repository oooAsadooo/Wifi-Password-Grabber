import subprocess


class Wifi_pass_grabber:

    def __init__(self):
        self.wifi_list = []

    def get_info_pass(self):
        name_pass = {}
        data = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for line in data:
            if 'All User Profile' in line:
                self.wifi_list.append(line.split(":")[-1][1:])
        for i in self.wifi_list:
            command = subprocess.getoutput(f'netsh wlan show profile "{i}" key=clear')
            if "Key Content" in command:
                split_key = command.split('Key Content')
                tmp = split_key[1].split('\n')[0]
                key = tmp.split(': ')[1]
                name_pass[i] = key
            else:
                key = ""
                name_pass[i] = key
        print(''' 
░██╗░░░░░░░██╗██╗███████╗██╗   ██████╗░░█████╗░░██████╗░██████╗██╗░░░░░░░██╗░█████╗░██████╗░██████╗░   ░██████╗░██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗   ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║   ██████╔╝███████║╚█████╗░╚█████╗░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║   ██║░░██╗░██████╔╝███████║██████╦╝██████╦╝█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║   ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░████╔═████║░██║░░██║██╔══██╗██║░░██║   ██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║   ██║░░░░░██║░░██║██████╔╝██████╔╝░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝   ╚██████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝   ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░   ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝     



                                                                                 Written By :~: ASAD   ''')
        print("For contacting Dm me on Discord , my discord id is => Asad#2809")
        print("              </> BooM <\>   \n")

        for i, j in name_pass.items():
            print(f'[*] SSID Name : "{i}" ==> Password :{j}')


pass1 = Wifi_pass_grabber()
pass1.get_info_pass()
