## ====IMPORTS====
import os
import requests
import platform
from colorama import Fore, Back, Style, init
import time
import sys


## ====VARIABLES====
Current_Name = os.path.basename(sys.executable)
Operative_System = None
App_Name = "NeuroTracker"
App_Version = 0.9
API_KEY = "HDEV-b2e657ea-f679-4f13-8545-e73e62f250be"


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
    ## UPDATE LINK
    update_link = "https://raw.githubusercontent.com/rubbennn/NeuroTracker/refs/heads/main/NeuroTracker.exe"

    ## .EXE
    exe = requests.get(update_link)

    ## Save File
    with open("NeuroTracker_New.exe", "wb") as f:
        f.write(exe.content)
        print(exe.status_code)
        print(exe.url)
        print(len(exe.content))

        time.sleep(2)

    ## Create Bat
    with open("update.bat", "w") as f:
        f.write(
            f"""
@echo off
timeout /t 2 /nobreak > nul
del "{sys.executable}"
ren "NeuroTracker_New.exe" "{Current_Name}"
timeout /t 2 /nobreak > nul
start {Current_Name}
del update.bat
"""
        )

    ## Start File
    os.startfile("update.bat")


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
    if not vrs:
        Clear()
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} An error has ocurred and {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE} must be restarted.\n")
        print(f"Press ENTER to quit.")
        exit()


    if vrs and vrs != App_Version:
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
        print(f"{Fore.LIGHTGREEN_EX}[✓] {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE} updated at last version [{Fore.LIGHTGREEN_EX}{App_Version}{Fore.WHITE}].\n")
        
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
        print(f"{Fore.LIGHTYELLOW_EX}[+]{Fore.WHITE} Internet Connection = {Fore.LIGHTRED_EX}False{Fore.WHITE}\n")
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} You must HAVE internet connection to use {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE}!\n")
        print(f"{Fore.LIGHTYELLOW_EX}[+] {Fore.WHITE}If this is an error, please restart {Fore.LIGHTBLUE_EX}{App_Name}{Fore.WHITE}.\n")
        input(f"Press ENTER to quit.")
        Clear()
        exit()
    

## ====SCRIPT====
# Get SO
Operative_System = GetSO()

# Start
Begining()
