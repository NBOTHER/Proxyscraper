import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy Scraper made by {Fore.WHITE}NoBother{Fore.LIGHTBLACK_EX} | ")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can find me on discord: {Fore.WHITE}NoBother#4508")


checker = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Ready to scrape? {Fore.WHITE}(yes){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if 'yes' in checker:
    typexd = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}What type of proxies do you want? {Fore.WHITE}(http, socks4, socks5, all){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")


if 'http' in typexd:
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    f = open('proxies.txt', 'w')
    f.write(res.text)
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}the {Fore.LIGHTBLACK_EX}proxies.")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The proxies was saved to: {Fore.WHITE}proxies.txt {Fore.LIGHTBLACK_EX}")
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Thanks for using this scraper. You are supporting us by using this.')
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Proxy info:')
    print(f'{Fore.WHITE} Type: Http')
    print(f'{Fore.WHITE} Proxy: Free')

if 'socks4' in typexd:
    res2 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500&ssl=yes')
    f = open('proxies.txt', 'w')
    f.write(res2.text)
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}the {Fore.LIGHTBLACK_EX}proxies.")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The proxies was saved to: {Fore.WHITE}proxies.txt {Fore.LIGHTBLACK_EX}")
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Thanks for using this scraper. You are supporting us by using this.')
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Proxy info:')
    print(f'{Fore.WHITE} Type: Socks4')
    print(f'{Fore.WHITE} Proxy: Free')

if 'socks5' in typexd:
    res3 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500&ssl=yes')
    f = open('proxies.txt', 'w')
    f.write(res3.text)
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}the {Fore.LIGHTBLACK_EX}proxies.")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The proxies was saved to: {Fore.WHITE}proxies.txt {Fore.LIGHTBLACK_EX}")
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Thanks for using this scraper. You are supporting us by using this.')
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Proxy info:')
    print(f'{Fore.WHITE} Type: Socks5')
    print(f'{Fore.WHITE} Proxy: Free')

if 'all' in typexd:
    res4 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=1500&ssl=yes')
    f = open('proxies.txt', 'w')
    f.write(res4.text)
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}the {Fore.LIGHTBLACK_EX}proxies.")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The proxies was saved to: {Fore.WHITE}proxies.txt {Fore.LIGHTBLACK_EX}")
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Thanks for using this scraper. You are supporting us by using this.')
    print(f"----------------------------")
    print(f'{Fore.YELLOW} Proxy info:')
    print(f'{Fore.WHITE} Type: All types')
    print(f'{Fore.WHITE} Proxy: Free')

input()