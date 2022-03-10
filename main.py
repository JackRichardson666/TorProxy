#inmports
from subprocess import Popen, PIPE
import requests
import subprocess
import sys

print('\n[+] starting...')

#proxy list for requests
proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}

#main
def init_proxy():
    print('\n[+] tor successfuly launched!')
    print('\n[+] checking the tor connection...')
    result_from_tor = requests.get('https://check.torproject.org/', proxies=proxies).text #Congratulations. This browser is configured to use Tor.
    if(result_from_tor.find('Congratulations. This browser is configured to use Tor.') == 166):
        print('\n[+] the check was successful! you can pass traffic through tor!')
    else:
        print('\n[!] the check was unsuccessful! please check config file or internet connection...')
        sys.exit(0);

#find func
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

#tor launcher
p = Popen(["Tor\\tor.exe", "-f", "Tor\\torrc"], stdout=PIPE)

for line in iter(p.stdout.readline, ''):
    linedecoded = line.decode("utf-8")
    if(linedecoded == ""):
        print('\n[!]', 'unable to start tor! restart the program')
        sys.exit(-1)
    print('[dbg]', '-> ', linedecoded)
    if(contains_word(linedecoded, 'Bootstrapped 100%')):print('\n[+] tor started!');init_proxy(),
p.stdout.close()