import os, re
from googletrans import Translator

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
print("    2. Separate dialogs into smaller files.")
print("    3. Translate the dialogues of an already extracted file.")
print("    4. Replace the dialogues with the translation.")
print("    5. Exit.")

number = int(input("\n(*) Number: "))

if number == 1:
    archive = str(input("\n(*) File to extract data(with the extension): "))

    dialogs = []
    with open(archive, 'r', encoding = "utf-8") as f:
        for dialogo in re.findall('\"(.*)\"', f.read()):
            #if dialogo not in dialogs:
            dialogs.append(dialogo)

    output = str(input("\n(*) Write the name of the output file(with the extension): "))
    f = open(output, 'w')
    f.write('\n'.join(dialogs))
    f.close
    print("\n(*) Successfully extracted dialogues.")

elif number == 2:
    archive = str(input("\n(*) File to Separate dialogs(with the extension): "))
    dir = str(input("\n(*) Name of the dir to make: "))

    os.mkdir(f'outputs/{dir}')

    lines_per_file = 50
    smallfile = None
    with open(archive) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'name{}.txt'.format(lineno + lines_per_file)
                smallfile = open(f'outputs/{dir}/{small_filename}', "w", encoding = "utf-8")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
    
    print("\n(*) Successfully separate dialogues.")
    
elif number == 3:
    dir = str(input("\n(*) Name of the created folder: "))
    language = int(input("\n(*) Choose the number of the language to which you want to translate:\n    1. Spanish\n    2. English\n    3. Russian\n(*) Number: "))
    output = str(input("\n(*) Write the name of the output file(with the extension): "))

    translator = Translator()

    filelist = os.listdir(f'outputs/{dir}/')
    archivos_unsort = []
    for file in filelist:
        if file[-4:] == '.txt':
            archivos_unsort.append(int(file.split('name')[1].split('.txt')[0]))
            archivos_unsort.sort()

    archivos = []
    for sort_num in archivos_unsort:
        for file in filelist:
            if str(sort_num) == file.split('name')[1].split('.txt')[0]:
                archivos.append(file)

    new = open(f'outputs/{dir}/{output}', 'a', encoding = "utf-8")
    new.write('\n')
    new.close()

    for file in archivos:
        with open(f'outputs/{dir}/{file}', 'r', encoding = "utf-8") as f:
            with open(f'outputs/{dir}/{output}', 'a', encoding = "utf-8") as end:
                message = f.read()
                if language == 1:
                    messagetrs = translator.translate(message, dest = 'es')
                    end.write('\n' + messagetrs.text)
                elif language == 2:
                    messagetrs = translator.translate(message, dest = 'en')
                    end.write('\n' + messagetrs.text)
                elif language == 3:
                    messagetrs = translator.translate(message, dest = 'ru')
                    end.write('\n' + messagetrs.text)
                else:
                    None

    print(f"\n(*) Successful translation of dialogues.\n(*) You can see the translation in 'outputs/{dir}/{output}'")

elif number == 4:
    archive = str(input("\n(*) File to extract data(with the extension): "))
    traduction = str(input("\n(*) File to extract traduction(with the extension): "))
    output = str(input("\n(*) Write the name of the output file(with the extension): "))

    with open(archive, "rt", encoding = "utf-8") as original:
        with open(traduction, "rt", encoding = "utf-8") as reemplazo:
            with open(output, "wt", encoding = "utf-8") as fin:
                for linea in original:
                    if '""' in linea:
                        linea = linea.replace('""', f'"{reemplazo.readline()}"')
                    fin.write(linea)
    print("\n(*) Successful translation of dialogues.")

else:
    None