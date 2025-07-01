import colorama
import os
import time

# Initialisation de colorama
colorama.init(autoreset=True)

# Logo ASCII
print(rf"""
$$$$$$$$\ $$\                       $$\                       $$\               $$\ $$\                     
\__$$  __|$$ |                      \__|                      $$ |              $$ |$$ |                    
   $$ |   $$$$$$$\   $$$$$$\        $$\ $$$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\  $$ |$$ | $$$$$$\   $$$$$$\  
   $$ |   $$  __$$\ $$  __$$\       $$ |$$  __$$\ $$  _____|\_$$  _|   \____$$\ $$ |$$ |$$  __$$\ $$  __$$\ 
   $$ |   $$ |  $$ |$$$$$$$$ |      $$ |$$ |  $$ |\$$$$$$\    $$ |     $$$$$$$ |$$ |$$ |$$$$$$$$ |$$ |  \__|
   $$ |   $$ |  $$ |$$   ____|      $$ |$$ |  $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |$$ |$$   ____|$$ |      
   $$ |   $$ |  $$ |\$$$$$$$\       $$ |$$ |  $$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$ |$$ |\$$$$$$$\ $$ |      
   \__|   \__|  \__| \_______|      \__|\__|  \__|\_______/    \____/  \_______|\__|\__| \_______|\__|      
""")

print(f"{colorama.Fore.RED}Les programmes sont en cours d'installation. Ne fermez pas la fenêtre.\n")

def run_installer(name, command):
    print(f"{colorama.Fore.WHITE}Installation de {name} en cours...")
    result = os.system(command)
    if result != 0:
        print(f"{colorama.Fore.RED}[ERREUR] L'installation de {name} a échoué (code {result})\n")
    else:
        print(f"{colorama.Fore.GREEN}[OK] {name} installé avec succès.\n")
    time.sleep(1)

# Installations
lenovo_vantage_ask = input("Voulez-vous installer Lenovo Vantage ?(y/n): ")
if lenovo_vantage_ask == "y":
    run_installer("Lenovo Vantage",r'winget install 9wzdncrfj4mv --accept-source-agreements --accept-package-agreements')
else:
    pass

run_installer("Vlc", r'cmd /c .\Apps\vlc-3.0.21-win64.exe /S')
run_installer("Adobe Reader", r'cmd /c ".\Apps\reader.exe /sAll /rs /msi EULA_ACCEPT=YES"')
run_installer("7-Zip",        r'cmd /c ".\Apps\7zip.exe /S"')
run_installer("Google Chrome",r'cmd /c ".\Apps\chrome.exe /silent /install"')
run_installer("LibreOffice",  r'cmd /c ".\Apps\LibreOffice.msi /quiet /norestart ALLUSERS=1"')

print(f"{colorama.Fore.BLUE}Toutes les installations sont terminées.")
