#!/usr/bin/env python3

# This program displays the HTTP headers of a website or
# or a file containing a list of websites, like this:
#
# cat file_urls.txt
# http://www.example1.com
# https://www.example2.com
# https://www.example3.com
#
#
# Based on the OWASP Secure Headers Project
# https://owasp.org/www-project-secure-headers/
#
# by Diego Moicano (@hihackthis)
# August 01st, 2022
# version 1.0
#
# Run:
# VSecHead.py -u/--url http(s)://www.example.com
# VSecHead.py -f/--file file_urls.txt
#
import argparse
import random
import requests
import os.path
from colorama import Fore, Style
from requests.exceptions import MissingSchema

sec_headers = [
    "HTTP Strict Transport Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "X-Permitted-Cross-Domain-Policies",
    "Referrer-Policy",
    "Clear-Site-Data",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Resource-Policy",
    "Cache-Control",
    "Permissions Policy"
]

dpr_headers = [
    "Feature-Policy",
    "Expect-CT",
    "Public-Key-Pins",
    "X-XSS-Protection"
]

user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/98.0.4758.82 Safari/537.36 OPR/84.0.4316.14",
    "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
]


# Here it fetch the website's HTTP headers and converts it into a list.
def fetch_headers(head):
    user_agent = random.choice(user_agents)
    ua_header = {"User-Agent": user_agent}
    response = requests.head(head, headers=ua_header)
    set_headers = response.headers
    keys_head = set_headers.keys()
    list_headers = list(keys_head)
    return list_headers


# Here it compares the list of headers found on the website with the list of secure headers.
def compare_sec_found(site, sec):
    new_head = []
    for header in site:
        if header in sec:
            new_head.append(header)

    if not new_head:
        return "Hey! Didn't you forget something?"
    elif True:
        jump_line = '\n'.join(map(str, new_head))
        return jump_line


# Here it compares the list of secure headers with the list of headers found on the website.
def compare_sec_miss(sec, site):
    new_head = []
    for header in sec:
        if header not in site:
            new_head.append(header)

    if not new_head:
        return "Good! No missing secure headers!"
    elif True:
        jump_line = '\n'.join(map(str, new_head))
        return jump_line


# Here it compares the list of headers found on the website with the list of deprecated headers.
def compare_dpr(site, dpr):
    new_head = []
    for header in site:
        if header in dpr:
            new_head.append(header)

    if not new_head:
        return "Good! No deprecated headers found!"
    elif True:
        jump_line = '\n'.join(map(str, new_head))
        return jump_line


# Here it enters the URL
def websites(url):
    try:
        check_result(url), sec_dpr(url), sec_miss(url), sec_found(url)
    except MissingSchema:
        print(f"\nEnter an entire URL (e.g http://{url} or https://{url})\n")
    except Exception as excpt:
        error = f"There was an error: {excpt}\n"
        print(Fore.RED, Style.BRIGHT, "\nERROR:", Style.RESET_ALL, error.split(":")[1])
        print("\t\tBe sure enter correct URL\n")


# Here it enters the file containing a list of websites
def file_urls(arq):
    file = os.path.isfile(arq)
    if file:
        with open(arq, "r", encoding="UTF-8") as urls:
            lines = urls.read().splitlines()
            for url in lines:
                try:
                    check_result(url), sec_dpr(url), sec_miss(url), sec_found(url)
                except MissingSchema:
                    print(Fore.RED, Style.BRIGHT, "\nERROR:", Style.RESET_ALL,
                          f"Enter an entire URL (e.g http://{url} or https://{url})\n")
                    continue
                except Exception as excpt:
                    error = f"There was an error: {excpt}\n"
                    print(Fore.RED, Style.BRIGHT, "\nERROR:", Style.RESET_ALL, error.split(":")[1])
                    print("\t\tBe sure enter correct URL\n")
                    continue
    else:
        print("Did you enter a right file or directory?\n")


# Display the URL(s)
def check_result(urls):
    print(end="\n")
    print(Fore.CYAN, Style.BRIGHT, ">>>", urls, Style.RESET_ALL)
    print(end="\n")
    print(Fore.LIGHTMAGENTA_EX, "[!] Check the results: ", Style.RESET_ALL)
    print(end="\n")


# Display deprecated headers
def sec_dpr(urls):
    print(end="\n")
    print(Fore.RED, Style.BRIGHT, "Deprecated Headers", Style.RESET_ALL)
    print("-----------------------------")
    res_head = compare_dpr(fetch_headers(urls), dpr_headers)
    new_list = list(res_head.split("\n"))
    for i in range(len(new_list)):
        print(Fore.RED, Style.BRIGHT, "[X]", Style.RESET_ALL, new_list[i])
    print(end="\n")


# Display missing headers
def sec_miss(urls):
    print(end="\n")
    print(Fore.YELLOW, Style.BRIGHT, "Secure Headers Missing", Style.RESET_ALL)
    print("-----------------------------")
    res_head = compare_sec_miss(sec_headers, fetch_headers(urls))
    new_list = list(res_head.split("\n"))
    for i in range(len(new_list)):
        print(Fore.YELLOW, Style.BRIGHT, "[>]", Style.RESET_ALL, new_list[i])
    print(end="\n")


# Display found headers
def sec_found(urls):
    print(end="\n")
    print(Fore.GREEN, Style.BRIGHT, "Secure Headers Found", Style.RESET_ALL)
    print("-----------------------------")
    res_head = compare_sec_found(fetch_headers(urls), sec_headers)
    new_list = list(res_head.split("\n"))
    for i in range(len(new_list)):
        print(Fore.GREEN, Style.BRIGHT, "[#]", Style.RESET_ALL, new_list[i])
    print(end="\n")


# Display my banner :-)
def banner():
    print("______ ________________________________ ______")
    print("  _____ _    ___         _  _             _ ")
    print(" |_   _| |  / __| ___ __| || |___ __ _ __| |")
    print("   | | | |__\__ \/ -_) _| __ / -_) _` / _` |")
    print("   |_| |____|___/\___\__|_||_\___\__,_\__,_|")
    print("\n______ _______ By @hihackthis _________ ______\n")
    # print("------")
    print(Fore.RED, Style.BRIGHT, "[X]".center(40), Style.RESET_ALL)
    print(Fore.YELLOW, Style.BRIGHT, "[>]".center(40), Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT, "[#]".center(40), Style.RESET_ALL, "\n")
    # print("------")


# Here is the menu
def main():
    parser = argparse.ArgumentParser(prog='TLSecHead.py',
                                     description="------ Traffic Light Secure Headers ------",
                                     formatter_class=argparse.RawTextHelpFormatter)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", help="enter URL [http:// | https://]")
    group.add_argument("-f", "--file", help="enter the file with URLs")
    args = parser.parse_args()

    if args.url:
        websites(args.url)
    elif args.file:
        file_urls(args.file)
    else:
        parser.print_help()
        exit()


# Call banner
banner()

# Call program
if __name__ == "__main__":
    main()
