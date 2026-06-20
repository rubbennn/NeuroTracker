## ====IMPORTS====
import os
import json
import requests
import platform
from colorama import Fore, Back, Style, init
import time


## ====VARIABLES====
Operative_System = None
App_Name = "NeuroTracker"
App_Version = 0.9

## {}
links = {
    "version": "https://raw.githubusercontent.com/rubbennn/NeuroTracker/main/Files/AppVersion.json"
}


## FUNCTIONS
def Title():
    print("""                                                                                 
,--.  ,--.                            ,--------.                     ,--.                  
|  ,'.|  | ,---. ,--.,--.,--.--. ,---.'--.  .--',--.--. ,--,--. ,---.|  |,-.  ,---. ,--.--. 
|  |' '  || .-. :|  ||  ||  .--'| .-. |  |  |   |  .--'' ,-.  || .--'|     / | .-. :|  .--' 
|  | `   |\   --.'  ''  '|  |   ' '-' '  |  |   |  |   \ '-'  |\ `--.|  \  \ \   --.|  |    
`--'  `--' `----' `----' `--'    `---'   `--'   `--'    `--`--' `---'`--'`--' `----'`--'                                                                                      
          """)

def CheckWifi():
    
    # Check if wifi
    try:
        requests.get("https://www.google.com", timeout=2)
        return True
    except requests.RequestException:
        return False


def GetSO():
    so = platform.system()
    
    # Check
    if so == "Windows":
        # Windows
        return "Windows"
    
        # Linux or MAC
    else:
        return "Linux"


def Clear():
    # Check if SO
    if Operative_System != None:
        
        if Operative_System == "Windows":
            # If Windows
            os.system("cls")
        
        else:
            # If not in Windows
            os.system("clear")
        
    else:
        print(f"{Fore.LIGHTRED_EX}[!] No operative system set!{Fore.WHITE}\n")


def UpdateApp():
    ### PLACE HERE TO UPDATE
    print("awd")


def ProgramStart():
    # Clear
    Clear()
    
    # Title
    Title()
    
    # Begin
    print(f"{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} Loading. . .\n")
    time.sleep(0.2)
    
    # Clear and Title
    Clear()
    Title()
    
    # Print
    print(f"{Fore.LIGHTGREEN_EX}[Example]:{Fore.WHITE} TheBest#1234\n")
    user = input(f"{Fore.LIGHTYELLOW_EX}[+] {Fore.WHITE}Valorant User: ")


def CheckVersion():
    
    vrs = requests.get(links["version"]).json()["version"]
    if vrs != App_Version:
        # Clear
        Clear()

        # Title
        Title()
        
        # Update
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} A new version of {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE} has been found!\n")
        print(f"{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} New Version: {Fore.LIGHTGREEN_EX}{vrs}{Fore.WHITE} [Current: {Fore.LIGHTGREEN_EX}{App_Version}{Fore.WHITE}]\n")
        Question = input("\n== Type S to update, or ENTER to skip: ").lower()
        if Question == "s":
            Clear()
            print(f"{Fore.LIGHTYELLOW_EX}[+] {Fore.WHITE}Updating {App_Name}.\n")
            UpdateApp()
        else:
            print(f"\n{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} Skipped new version.\n")
            time.sleep(0.2)
            ProgramStart()
            
    else:
        print(f"{Fore.LIGHTGREEN_EX}[✓] {Fore.WHITE}{App_Name} updated.\n")
        
        # Start!
        ProgramStart()
    



def Begining():
    # Clear
    Clear()
    
    # Title
    Title()
    
    # Begin
    print(f"{Fore.LIGHTYELLOW_EX}Initializing {Fore.LIGHTBLUE_EX}{App_Name}{Fore.LIGHTYELLOW_EX}. . .{Fore.WHITE}\n")

    # Check if wifi first
    if CheckWifi():
        # Internet
        print(f"{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} Internet Connection = {Fore.LIGHTGREEN_EX}True{Fore.WHITE}\n")
        
        # Check Version
        print(f"{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} Checking {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE} version. . .\n")
        time.sleep(0.2)
        CheckVersion()
    
    else:
        # No internet
        print(f"{Fore.WHITE}[+] Internet Connection = {Fore.LIGHTRED_EX}False{Fore.WHITE}\n")
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} You must HAVE internet connection to use {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE}!\n")
        input(f"Press ENTER to quit.")
        Clear()
        exit()
    

## ====SCRIPT====
# Get SO
Operative_System = GetSO()

# Start
Begining()
