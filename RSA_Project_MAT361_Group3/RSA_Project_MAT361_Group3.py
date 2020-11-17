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
blocksize=128//8
d=231371739696627534045915232632172695126683


# Global information
IS_ENCRYPTING = ""
FILEPATH = os.path.dirname(os.path.realpath(__file__))
IN_DATA = ""
BLOCKS = []
OUT_DATA = ""

# Functions
def Modexp(a,x,m):
    a = a % m
    counter = 1
    while x > 0:
        if x % 2 == 1:
            counter *= a
            counter %= m
        a **= 2
        a %= m
        x //= 2
    return counter

def Encode(message):
    block = 0
    encoded = []
    for i in range(0,len(message)):
        block = block * 100 + message[i]

        if (i+1) % blocksize == 0:
            encoded.append(block)
            block = 0
    # there may be an incomplete block
    if block > 0:
        encoded.append(block)

    return encoded 

def Encrypt(message):
    encoded = Encode(message)
    out = ""
    for i in range(0,len(encoded)):
        out+=str(Modexp(encoded[i],e,n))
    return out

def Decrypt(encrypted):
    return Modexp(int(encrypted),d,n)

### Run Program ###

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
IN_DATA = open(FILEPATH, "rb").read()

# Encode (plain text -> blocks ready for encryption)
OUT_DATA = Encrypt(IN_DATA)
encryptedFile = open('encrypted.txt', 'w')
encryptedFile.write(OUT_DATA)
encryptedFile.close()
# Decrypt (decrpyt back into blocks)
# Decode (blocks -> plaintext)


