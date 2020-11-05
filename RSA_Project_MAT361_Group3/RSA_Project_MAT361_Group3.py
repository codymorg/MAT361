########################################
# RSA Project - Group3                 #
# MAT361                               #
# 5 NOV 2020                           #
# Charles Eichelberger                 #
# Joseph McDonell                      #
# Cody Morgan                          #
########################################

import os #displaying folder contents

# This will never change for this project 
n=777171741032261716925235958354065598504223
e=131
b=128
d=231371739696627534045915232632172695126683

# Global information
IS_ENCRYPTING = ""
FILEPATH = os.path.dirname(os.path.realpath(__file__))
IN_DATA = ""

# User input to select encryption or decryption
while (len(IS_ENCRYPTING) == 0 or (IS_ENCRYPTING != "E" and IS_ENCRYPTING != "D")):
    print("[E]ncrpyt or [D]ecrypt?")
    IS_ENCRYPTING = input()[0].upper()
    print("")

# User input to select file
while (len(FILEPATH) > 0):
    print("\n>>"+FILEPATH)
    dir = os.listdir(FILEPATH)
    i=0
    print("[..]: previous directory")

    for file in dir:
        isDir = os.path.isdir(FILEPATH + "\\" + file)
        print("[",i,"]:","{DIR}  "if isDir else "{FILE} ",file)
        i+=1

    userInput = input()
    # navigate up
    if ".." in userInput:
        folders = FILEPATH.split("\\")
        FILEPATH = ""
        for i in range(0, len(folders)-1):
            FILEPATH += folders[i] + ("\\" if i < len(folders)-2 else "") #dont add \\ to the last folder
    
    # see if input is a file selection
    else:
        try:
            possible = int(userInput)
            FILEPATH += "\\" + dir[possible]
            if os.path.isfile(FILEPATH):
                break # we're done if a file is chosen
        except:
            print("Please enter valid file number\n")
IN_DATA = open(FILEPATH, "r")


# Encode (plain text -> blocks ready for encryption)
# Encrypt (RSA encrypt)

# Decrypt (decrpyt back into blocks)
# Decode (blocks -> plaintext)


