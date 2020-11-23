########################################
# RSA Project - Group3                 #
# MAT361                               #
# 5 NOV 2020                           #
# Charles Eichelberger                 #
# Joseph McDonell                      #
# Cody Morgan                          #
########################################

import os #displaying folder contents
import math

# This will never change for this project 
n=777171741032261716925235958354065598504223
e=131
blocksize=14
d=231371739696627534045915232632172695126683
b_3 = 3456273625187339
p_3 = 11111311111233333600700633333211111311111
r = 2184169779496
k = 20653351956439504081

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
        block = block * 1000 + message[i]
        if (i+1) % blocksize == 0:
            encoded.append(block)
            block = 0
    # there may be an incomplete block
    if block > 0:
        encoded.append(block)
    print("encoded",encoded[0])
    return encoded 

def Encrypt(message):
    encoded = Encode(message)
    while len(str(encoded[len(encoded)-1])) < (3*blocksize-2):
        encoded[len(encoded)-1] = (encoded[len(encoded)-1]*1000) + 999
    out = ""
    for i in range(0,len(encoded)):
        out+=str(Modexp(encoded[i],e,n))
        if i<len(encoded)-1:
            out += " "
    return out

def Decrypt(encrypted):
    return Modexp(int(encrypted),d,n)

def Modinverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
        q = a // m 
  
        t = m 
        m = a % m 
        a = t 
        t = y 
  
        y = x - q * y 
        x = t 
  
    if (x < 0): 
        x = x + m0 
  
    return x 

def ElGamalSignature():
  rk = Modexp(r, k, p_3)
  rb = Modexp(r,b_3,p_3)
  m = 2020
  out = ""
  out += "p = "
  out += str(p_3)
  out += "\n"
  out += "r = "
  out += str(r)
  out += "\n"
  out += "m = 2020\n"
  out += "r^b = "
  out += str(rb)
  out += "\n"
  out += "r^k = "
  out += str(rk)
  out += "\n"
  out += "s = "

  a = b_3 * rk
  b = m - a

  multinverse = Modinverse(k, p_3 - 1)

  temp = (b * multinverse) % (p_3 - 1)
  out += str(temp)
  return out

def RSASignature():
  out = ""
  m = 2020
  out += "N = "
  out += str(n)
  out += "\n"
  out += "e = "
  out += str(e)
  out += "\n"
  out += "m = "
  out += str(m)
  out += "\n"
  out += "m^d = "
  out += str(Modexp(m,d,n))
  return out


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

ElGAMELSIGNATURE_DATA = ElGamalSignature()
elGamelSignatureFile = open('elgamelsignature.txt', 'w')
elGamelSignatureFile.write(ElGAMELSIGNATURE_DATA)
elGamelSignatureFile.close()

RSASIGNATURE_DATA = RSASignature()
rsaSignatureFile = open('rsasignature.txt', 'w')
rsaSignatureFile.write(RSASIGNATURE_DATA)
rsaSignatureFile.close()
# Decrypt (decrpyt back into blocks)
# Decode (blocks -> plaintext)


