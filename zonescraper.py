import colorama
from colorama import Fore as F, init

colorama.init(autoreset=True)
import requests
import bs4
from bs4 import *
from random import choice
import sys, re
from console.utils import set_title

print(" welcome to my grabber please make sure you run the following commandes:")
print(F.GREEN + "\n- pip install colorma\n- pip install requests\n- pip install bs4\n- pip install console ")
print(F.LIGHTGREEN_EX + " \n [my telegram : @waliidsh] \n  DM ME FOR TOOLS AND UPDATES")
print("\n\n- [1] grabbe links from zone-h.org")

var = int(input("==>"))
if var == 1:

    class website:
        website = 0


    class lets_start():
        def __init__(self) -> None:
            self.web = 0
            self.green = F.GREEN
            self.logo = self.green + """
                   \n
                   [+] WELCOME BOY\n
                   [+] GET COOKIES FROM ZONE-H.ORG !\n
                   [+] DON'T FORGOT TO SOLVE THE CAPTCHA ON YOUR BROWSER
                   """

        def grab(self):
            print(self.logo)
            print(F.LIGHTYELLOW_EX + "\nEntre Cookies HERE :")
            var11 = input("Entre PHPSESSID: ")
            var22 = input("Entre ZHE: ")
            var88 = {
                "ZHE": var22,
                "PHPSESSID": var11
            }
            for qwd in range(1, 51):
                var60 = requests.get("http://zone-h.org/archive/published=0" + "/page=" + str(qwd), cookies=var88)
                dzq = var60.text
                if '''<html><body>-<script type="text/javascript"''' in dzq:
                    print(input(F.RED +"\nWRONG COOKIES MAN"))
                    sys.exit()
                elif "captcha" in dzq:
                    print(" ENTER THE CAPTCHA ON YOUR BROWSER AND TRY AGAIN")
                else:
                    Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
                    self.web += 1
                    for xxx in Hunt_urlss:
                        qqqq = xxx.replace('...', '')
                        print(F.GREEN+'    [' + '*' + '] ' + qqqq.split('/')[0])
                        with open('result.txt', 'a') as rrr:
                            rrr.write("http://" + qqqq.split('/')[0] + '\n')
            set_title(f'GRABBER FROM ZONE H | WEBSITE = [{self.web}]')


    if __name__ == '__main__':
        start = lets_start()
        start.grab()