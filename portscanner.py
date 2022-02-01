import socket,colors,time,sys,threading,argparse
import concurrent.futures 
from datetime import datetime
from colorama import Fore
print_lock = threading.Lock()
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',metavar='',help='IP of the target or domain. (Ex. google.com)')
parser.add_argument('-pl','--portlimit',metavar='',help='Number limit of the port scanning. (Ex. 1000)')
parser.add_argument('-th','--threads',metavar='',help='Number of threads/workers. (default: 100)', default=100)
args = parser.parse_args()
class PortScanner(object):
    def __init__(self,target,portl,threads):
        self.target = target
        self.portl = portl
        self.threads = threads
    def banner(self):
       now = datetime.now()
       dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
       print(f"""{colors.BGreen}
╔╦╗┬ ┬┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐
 ║ ├─┤├┬┘├┤ ├─┤ ││├┤  ││  ╠═╝│ │├┬┘ │   ╚═╗│  ├─┤││││││├┤ ├┬┘
 ╩ ┴ ┴┴└─└─┘┴ ┴─┴┘└─┘─┴┘  ╩  └─┘┴└─ ┴   ╚═╝└─┘┴ ┴┘└┘┘└┘└─┘┴└─
               """) 
       print(Fore.WHITE + "─" * 38)
       print(f"{Fore.GREEN}Github: {Fore.WHITE}https://github.com/FonderElite")
       print(Fore.WHITE + "─" * 38)
       time.sleep(0.3)
       print(f"{Fore.WHITE}Scanning Target: {Fore.GREEN}{self.target}")
       time.sleep(0.5)
       print(f"{Fore.WHITE}Script started at: {Fore.GREEN}{str(dt_string)}{Fore.WHITE}")       
       if args.target == None or args.portlimit == None:
           pass
       else:
           time.sleep(0.5)
           print(f"{Fore.WHITE}]Port Range: {Fore.GREEN}1{Fore.WHITE}-{Fore.GREEN}{self.portl}")
           time.sleep(0.3)
           print(f"{Fore.WHITE}Threads:{Fore.GREEN} {self.threads}\n")
    def scan_ports(self,port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        scanner.settimeout(1)
        try:
            scanner.connect((self.target,port))
            scanner.close()
            with print_lock:
                print(f'{colors.BWhite}[{colors.BGreen}+{colors.BWhite}]Open Port: {port}')
                if  port == 21:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]FTP\n")
                elif port == 22:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]SSH/FTPS\n")
                elif port == 25:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]SMTP\n")
                elif port == 80:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]HTTP\n")
                elif port == 110:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]POP3\n")
                elif port == 143:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]IMAP\n")
                elif port == 161:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]SNMP(Simple Network Management Protocol)\n")
                elif port == 443:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]HTTPS\n")
                elif port == 587:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]SMTP SSL\n")
                elif port == 993:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]IMAP SSL\n")
                elif port == 995:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]POP3 SSL\n")
                elif port == 2082:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]CPANEL\n")
                elif port == 2083:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]CPANEL SSL\n")                
                elif port == 2086:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]WHM(Web Host Manager)\n")
                elif port == 2087:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]WHM SSL(Web Host Manager) \n")
                elif port == 2095:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]WEB-MAIL\n")
                elif port == 2096:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}{Fore.WHITE}]WEB-MAIL SSL\n")
                elif port == 2077:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]Web-DAV/Web-DISK\n")
                elif port == 2078:
                    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]Web-DAV/Web-DISK SSL\n")
        except KeyboardInterrupt:
            print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]Exiting Program.")
            sys.exit()
        except socket.gaierror:
            print(f"{WHITE}[{Fore.RED}-{Fore.WHITE}]Hostname Could Not Be Resolved.")
            sys.exit()
        except socket.error:
            pass

if __name__ == "__main__":
    call_class = PortScanner(args.target,args.portlimit,args.threads)
    banner = call_class.banner()
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(args.threads)) as executor:
            for port in range(int(args.portlimit)):

                executor.submit(call_class.scan_ports,port + 1)
    except TypeError:
        print(f"{Fore.GREEN}Usage: {Fore.CYAN}python3 {Fore.WHITE}<portscanner.py> {Fore.GREEN}-t {Fore.WHITE}<target> {Fore.GREEN}-pl {Fore.WHITE}<port-limit>")



