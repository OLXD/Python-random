#!/usr/bin/env python3
import colorama
from colorama import Back, Fore
colorama.init(autoreset = True)
text = input("Enter a pharse or sentence: ")
print(Fore.RED + text)
print(Back.RED + text)
print(Fore.BLACK + Back.WHITE + text)
print(Fore.RED + Back.CYAN + text)
print(Fore.GREEN + Back.MAGENTA + text)
print(Fore.YELLOW + Back.BLUE + text)
print(Fore.BLUE + Back.YELLOW + text)
print(Fore.MAGENTA + Back.GREEN + text)
print(Fore.CYAN + Back.RED + text)
print(Fore.WHITE + Back.BLACK + text)

