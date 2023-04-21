# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Lab Exercise 1 - Problem 2


# import modules
import pyfiglet
import colorama
from colorama import Fore, Style
import time

# Create a try-again function to use the program again if the user wants to 
def try_again():
    retry = None
    while retry is None:
        time.sleep(1)
        again = input(Fore.MAGENTA + "\n\t\t\tDo you want to try again? (YES/NO)  ")
        # the program will run again if the user inputted YES
        if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
            retry = str(again)
            continue
        # the program will terminate if the user inputted NO
        if again == "N" or again == "No" or again == "NO" or again == "no":
            time.sleep(0.5)
            print(Fore.GREEN + "\t\t\t[Program will be terminated..............]")
            time.sleep(1.5)
            print("\n")
            print("\033[0;34m" + "\033[1m-" * 140 + '\033[0m')
            print(" ")
            lab = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 140, justify = "center")
            print(Style.BRIGHT + Fore.CYAN + lab)
            exit()
        else:
            print(Fore.RED + "\t\t\t[ERROR] Please choose either YES or NO only.")


# Use pyfiglet formatting to "Lab. Exercise No. 1"
print("")
lab = pyfiglet.figlet_format("LAB EXERCISE # 1", font = "banner3-d", width = 141, justify = "center")
print(Style.BRIGHT + Fore.CYAN + lab)

# format introductory message

# insert time delay

# while loop
    # ask user to input the encrypted text
    # replace each character ( '* to a', '& to e', '# to i', '+ to o', '! to u' )
    # display decrypted text

    # call try-again function