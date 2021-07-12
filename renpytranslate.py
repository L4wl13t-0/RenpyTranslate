import os, re

os.system('cls' if os.name == 'nt' else 'clear')
A = '''
    ______ _____ _   _ ________   __
    | ___ \  ___| \ | || ___ \ \ / /
    | |_/ / |__ |  \| || |_/ /\ V / 
    |    /|  __|| . ` ||  __/  \ /  
    | |\ \| |___| |\  || |     | |  
    \_| \_\____/\_| \_/\_|     \_/
         ___________  ___   _   _  _____ _       ___ _____ _____ 
        |_   _| ___ \/ _ \ | \ | |/  ___| |     / _ \_   _|  ___|
          | | | |_/ / /_\ \|  \| |\ `--.| |    / /_\ \| | | |__  
          | | |    /|  _  || . ` | `--. \ |    |  _  || | |  __| 
          | | | |\ \| | | || |\  |/\__/ / |____| | | || | | |___ 
          \_/ \_| \_\_| |_/\_| \_/\____/\_____/\_| |_/\_/ \____/ 


            Renpy Translate (V0.1) coded by Lawliet.
    '''
print(A+"\n")

print("(*) Choose the number of the operation to perform:")
print("    1. Extract the dialogs from a .rpy file.")
print("    2. Translate the dialogues of an already extracted file.")
print("    3. Directly extract and translate the dialogues. (1 - 2)")
print("    4. Exit.")

number = int(input("\n(*) Number: "))

if number == 1:
    archive = str(input("\n(*) File to extract data(with the extension): "))

    dialogs = []
    with open(archive, 'r') as f:
        for dialogo in re.findall('\"(.*)\"', f.read()):
            if dialogo not in dialogs:
                dialogs.append(dialogo)

    output = str(input("\n(*) Write the name of the output file: "))
    f = open(output, 'w')
    f.write('\n'.join(dialogs))
    f.close
    print("\n(*) Successfully extracted dialogues.")