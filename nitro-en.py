from os import name, chdir, rmdir, mkdir, rename, listdir
from os.path import isdir
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import choice, shuffle, randint
from binascii import hexlify
from shutil import rmtree
from colorama import Fore, init
from os import system as cmd
from time import sleep
import ctypes
import random
import string
import platform

try:
    import colorama
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

banner1 = """
                        hNNNNmmdhys+/-.                                 
                       `NMNsoosyyhmNMMMNmyo/.                           
                       -MMo       ```-/oydNMNmy+-`                      
                       oMM-              ``-+ymMNmy/.                   
                       mMm                    `-+hmMNh/                 
                      /MMo                        .sMMm                 
           :s/.      `mMMmdddhyso+/-..`           `hMN-                 
           omMNh+-`  oMMMMMMMMMMMMMMNmdyo/-`      +MM+                  
            ./ymNNdyoNMMMMMMMMMMMMMMMMMMMMNmh+-` `NMd                   
               `:ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMmyyMM:                   
                   `-dMMNNMMMMMMMMMMMMMMMMMMMMMMMMMm                    
                     sMM--/oydNMMMMMMMMMMMMMMMMMMMMy``````-.            
                     sMM.      `-:+oyhmNMMMMMMMMMMMMNNNMMMMM:           
                  -+hMMh  `ohhy.         `..:oMMh///////::-.            
              -+hNMMmy/   +MMMMd             sMM-                       
          `:smNMmy+.`     .hmmd/            .NMd                        
        -omNMdo-`           ```            `dMN-                        
     `/hNMdo-`                            -dMN/                         
   `/dMNh:`           ``.......``      `-yNMd-                          
  -dMNy-       `.-/oyhdmmmmmmmmmddhs++sdNNd+`                           
 /NMd:    `.:oydNMMMMMMMMMMMMMMMMMMMMMNdo:`                             
:NMh` `./sdNMMMMMMMMMMMMMMMMMMMMMNmdo/.                                 
mMN-:sdNMMMMMMMNNNmdhysoosyhdmdh+:`                                     
MMNmMMMMNNdyo+/-.`"""[1:].replace('M', '0')


banner2 = """                           
                         .-:+oyyhhddmmmmmmmmo                           
                    .:+sydmmmmmmmmmmmmmmmmmmh                           
               .:oyhmmmmmmmmmmmmmmmmmmmmmmmmm.                          
            :ohmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm/                          
         /ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms                          
        +mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd`                         
        `hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm:                         
         .dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms         -/osyyo         
          /mmmmmmmmmmmmmmmmmmmmmmmmmdhysso+/:yd`    -+yddmmmmmd`        
           ymmmmmmmmmmmmmmmmmdhyo+:-.``      :m+-/shdmmmmmmmds.         
           .dmmmmmmmmmmdhyo/-.`           `.:+mddmmmmmmmmdy+.           
            /mmmmmdhy+:.`         `..-/+syhddmmmmmmmdhyo:.`             
            `ymdy+-.    ``..-:/+syhhdmmmmmmmmmmmdyo/-.                  
   ..-:::::--/hy://++osyyhhdmmmmmmmmmmmmddhhs++m:                       
.ohdmmmmdddhhhhhhdddmmmdhhhhmmdddddhyso++/:.` .h:`                      
smmmmmmhsydyhhhhydysdmdsyhhys+/::-.`  -yhshd+``/o/-`                    
`+yddddyshyhysoyyhhsdmdso`           `ohmdhhy`` .+s++/`                 
    `.......`  -ydysdmdys`           `/hdyhhs       -+oo+`              
               `ddhhdmmmd:             /syy+`          ./yy/`           
                ommmmmmmmh`                               .+ho.         
                .dmmmmmmmms                                 `/ys.       
                 /mmmmmmmmms`                                 `/yo`     
                  ommmmmmmmmhyyyhhhhyyysssoo+/::-.`             `oh:    
                  `ommmmmmmmmmmy-...........-::/+ooso+:-`         :h+   
                    /dmmmmmmmmmdho/:----:://++++++++++syys/-`      -ho  
                     -mmmmmmmmmmmmmmmmmds+/:------:://++oyhhho:.    -ho 
                    `+mmmmmmmmmmmmmmmmm/                  `.-/sss/.` -d:
                   -smmmmmmmmmmmmmmmmmms`                      `./ss++ds
                 `+dmmmmmmmmmmmmmmmmmmmmh:`                        .:/:`
                `ymmmmmmmmmmmmmmmmmmmmmmmmy:`                           
                `oddmmmmmmmmmmmmmmmmmmmmmmmmy                           
                   -/oydmdmmmmmmmmmmmmmmhyo/.                           
                         ..-::::::::-..                 Press ENTER to open Nitro Gen options"""[1:].replace('m','0')


banner = choice((banner1, banner2))

# __import__('pyperclip').copy('\n'.join(l.rstrip() for l in banner.splitlines()))

ascii = '''
▄▄▄▄·  ▄· ▄▌  ·▄▄▄▄  ▪  ▄▄▄ . ▄▄ •       
▐█ ▀█▪▐█▪██▌  ██· ██ ██ ▀▄.▀·▐█ ▀ ▪ ▄█▀▄ 
▐█▀▀█▄▐█▌▐█▪  ▐█▪ ▐█▌▐█·▐▀▀▪▄▄█ ▀█▄▐█▌.▐▌
██▄▪▐█ ▐█▀·  .██. ██ ▐█▌▐█▄▄▌▐█▄▪▐█▐█▌.▐▌
·▀▀▀▀   ▀ •   ▀▀▀▀▀• ▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪'''[1:]


def init():
    System.Clear()
    System.Title("ByDiego | Nitro Generator")
    System.Size(100, 40)
    Anime.Fade(text=Center.Center(banner2), color=Colors.red_to_black, mode=Colorate.Diagonal, enter=True)

ctypes.windll.kernel32.SetConsoleTitleW(
    "Discord Nitro Generator | ByDiego | v1.0")

nitros = open("nitros-bydiego.txt", "a")

def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
    print('\n'*3)
    print(f"{Fore.WHITE}[ {Fore.CYAN}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator Creado Por {Fore.WHITE}ByDiego{Fore.LIGHTBLACK_EX} | {Fore.WHITE}I am not responsible for the use of this tool{Fore.RESET}\n{Fore.WHITE}[ {Fore.CYAN}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Follow Me On: {Fore.WHITE}https://github.com/zByDiegoTM{Fore.RESET}")
    try:
        try:
            nitroAmount = int(input(
                f"\n{Fore.WHITE}[ {Fore.RED}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How many codes you want generate?: {Fore.WHITE}"))
        except ValueError:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The amount must be {Fore.WHITE}a number")
            sleep(2)
            return main()

        nitroType = input(f"{Fore.WHITE}[ {Fore.RED}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}What type of nitro you want generate? {Fore.WHITE}classic {Fore.LIGHTBLACK_EX}o {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}? (El Nitro Classic contiene 16 charácteres de palabras y el Nitro Boost contiene 24): {Fore.WHITE}")

        if nitroType == "boost" or nitroType == "classic":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}The answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}o {Fore.WHITE}classic{Fore.RESET}")
            sleep(2)
            return main()

        nitroLink = input(
            f"{Fore.WHITE}[ {Fore.RED}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Do you want {Fore.WHITE}https://discord.com/gifts/ {Fore.LIGHTBLACK_EX}behind the codes ? ({Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no): {Fore.WHITE}")

        if nitroLink == "yes" or nitroLink == "no":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You must respond {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no{Fore.RESET}")
            sleep(2)
            return main()
    except KeyboardInterrupt:
        clear_console()
        exit()

    gen(nitroAmount, nitroType, nitroLink)


def gen(nitroAmount, nitroType, nitroLink):

    amount = 0

    with open("nitros-bydiego.txt", "w") as file:
        file.write("")

    for _ in range(nitroAmount):
        genCode = "".join(random.choice(string.digits+string.ascii_letters)
                          for _ in range(24)) if nitroType == "boost" else "".join(random.choice(string.digits+string.ascii_letters)
                                                                                   for _ in range(16))
        nitro = f"https://discord.com/gifts/{genCode}" if nitroLink == "yes" else genCode

        try:
            print(
                f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.RESET}{nitro}")
            nitros.write(
                f"{nitro}\n")
            amount += 1
        except:
            break

    nitros.close()
    input(
        f"\n{Fore.WHITE}[ {Fore.RED}> {Fore.WHITE}] {amount} nitros have been successfully generated. Has been saved in (nitros-bydiego). (Press a ENTER to return main menu)")


def clear_console():
    if platform.system() == "Windows":
        cmd("cls")
    else:
        cmd("clear")





if __name__ == '__main__':
    init()
    while True:
        main()
