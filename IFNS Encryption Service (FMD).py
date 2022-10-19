from time import sleep
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10000)

print('''



   IFNS-ES (加密/解密系統) 版本M16.3.6(Beta) is Starting...
   ----------------------------------------------------

''') ; sleep(2)
print('''
   NOTICE: Please use Python 3.10 or ABOVE for FULL ENCRYPTION/DECRYPTION services, in order
   for the application to run, please install "pip" and "colorama" extension on your PC.
   ---------------------------------------------------------------------------------------

   Links below:
   How to install pip on Windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
   How to install colorama in python: https://stackoverflow.com/questions/9846683/how-to-install-colorama-in-python

   (You're currently using a MOBILE beta version, some programs might not work as expected.)''') ; sleep(3)


while True:
    a = input('''
   Would you like to skip tasklist scan? yes/no : ''')
    if a=="yes":
        print('''
   *The beta version doesn't support skipping tasklist.''')
        continue
    elif a=="no":
        break
    else:
        print('''
   Enter either yes/no''')


print('''


    Loading Tasklist Chart...
    ----------------------
    ''') ; sleep(2)

print('''    Volume in IFNS-HD is IFNS_DISK
     Directory of IFNS-HD:\
''') ; sleep(1.5)
print('''


    IO       SYS*   223148   7-11-95   9:50a
''') ; sleep(1)
slowprint('''    IFNS  SYS*        4   7-11-95   9:50a      4:13/2145721
    COMMAND  COM     92870   7-11-95   9:50a    |   PRECOPY1 CAB    484352   7-11-95   9:50a
    AUTOEXEC BAT        25   7-11-95   9:50a    |   WB16OFF  EXE       537   7-11-95   9:50a
    CONFIG   SYS        40   7-11-95   9:50a    |   SCANDISK EXE    134738   7-11-95   9:50a
    COUNTRY  SYS     27094   7-11-95   9:50a    |   DOSSETUP BIN     72246   7-11-95   9:50a
    DISPLAY  SYS     17175   7-11-95   9:50a    |   WINSETUP BIN    159504   7-11-95   9:50a
    EGA      CPI     58870   7-11-95   9:50a    |   DELTEMP  COM       496   7-11-95   9:50a
    EGA2     CPI     58870   7-11-95   9:50a    |   SAVE32   COM       920   7-11-95   9:50a
    EGA3     CPI     48973   7-11-95   9:50a    |   EXTRACT  EXE     46656   7-11-95   9:50a
    FDISK    EXE     59128   7-11-95   9:50a    |   OK~ ------------------------------------
    FORMAT   COM     40135   7-11-95   9:50a    |   
    HIMEM    SYS     32935   7-11-95   9:50a    |   
    KEYB     COM     19927   7-11-95   9:50a    |   
    KEYBOARD SYS     34566   7-11-95   9:50a    |   
    KEYBRD2  SYS     31942   7-11-95   9:50a    |   
    MODE     COM     29191   7-11-95   9:50a    |   
    OEMSETUP BIN      3270   7-11-95   9:50a    |   
    OEMSETUP EXE     78668   7-11-95   9:50a    |   
           19 file(s)     856831 bytes

                      595968 bytes free''') ; sleep(1.5)
print('''
    ---------------------------------------------------------------------------------------
''')
slowprint('''    MINI     CAB    441905   7-11-95   9:50a   4:14/2160126
    PRECOPY1 CAB    484352   7-11-95   9:50a    |   EGA      CPI     58870   7-11-95   9:50a
    WB16OFF  EXE       537   7-11-95   9:50a    |   WINVER   TSI     95820   7-11-95   9:50a
    SCANDISK EXE    134738   7-11-95   9:50a    |   MACAFEE  VIR    274210   7-11-95   9:50a
    DOSSETUP BIN     72246   7-11-95   9:50a    |   OK~ ------------------------------------
    WINSETUP BIN    159504   7-11-95   9:50a    |
    DELTEMP  COM       496   7-11-95   9:50a    |
    SAVE32   COM       920   7-11-95   9:50a    |
    EXTRACT  EXE     46656   7-11-95   9:50a    |
    SCANPROG EXE      4438   7-11-95   9:50a    |
    SETUP    EXE      5184   7-11-95   9:50a    |
    SMARTDRV EXE     45145   7-11-95   9:50a    |
    XMSMMGR  EXE     14144   7-11-95   9:50a    |
    SCANDISK PIF       995   7-11-95   9:50a    |
    README   TXT      7302   7-11-95   9:50a    |
    SETUP    TXT     34612   7-11-95   9:50a    |
           16 file(s)    1453174 bytes

                               2513210 bytes free


                           ''') ; sleep(3)

print('''       Exiting Tasklist Check...
      --------------------------''') ; sleep(2)


A = print('''    Volume in drive IFN-HD is DISK13
     Directory of A:\

    IFNS_13 CAB    981813   7-11-95   9:50a
            1 file(s)     981813 bytes
                      733184 bytes READY...

''') ; sleep(3)
print('''       Startup Complete... Loading System...
    --------------------------------------------''') ; sleep(4)
print('''

    IFN 1.0.2 (v1.0.2:6503f05dd5) 
    [Tlang 3.0 (tlang-800.0.59)] on darwin
    IFNS Encrypttion service secure... Germany...
    -----------------------------------------------------

''')

#Encrypter 
from time import sleep


plain_text = input ('''      1E- Enter message to be ENCRYPTED : ''')
print(''' 
    ''')

encrypted_text = ""

for letter in plain_text:
    
    com_letter = ord(letter)
    
    com_letter = (com_letter) + 1
    
    reverse = chr(com_letter)
    
    encrypted_text = encrypted_text + str(reverse)

print('''
      Your encrypted message is : ''',encrypted_text)  ; sleep(3)  

#Decryption Sevice
enter_encrypted_text = input('''


      1D- Enter message to be DECRYPTED : ''')
print(''' 
    ''')

decrypted_text = ""

for char in enter_encrypted_text:
    
    com_char = ord(char)
    
    com_char = (com_char) - 1
    
    reverser = chr(com_char)
    
    decrypted_text = decrypted_text + str(reverser)
    
print('''
      Your decrypted message is : ''',decrypted_text) ; sleep(3)

plain_text = input ('''
     -----------------------------------------------------


      2E- Enter message to be encrypted : ''')
print(''' 
    ''')

encrypted_text = ""

for letter in plain_text:
    
    com_letter = ord(letter)
    
    com_letter = (com_letter) + 1
    
    reverse = chr(com_letter)
    
    encrypted_text = encrypted_text + str(reverse)

print('''
      Your encrypted message is : ''',encrypted_text)  ; sleep(3)  

#Decryption Sevice
enter_encrypted_text = input('''


      2D- Enter message to be decrypted : ''')
print(''' 
    ''')

decrypted_text = ""

for char in enter_encrypted_text:
    
    com_char = ord(char)
    
    com_char = (com_char) - 1
    
    reverser = chr(com_char)
    
    decrypted_text = decrypted_text + str(reverser)
    
print('''
      Your decrypted message is : ''',decrypted_text) ; sleep(3)

plain_text = input ('''
     -----------------------------------------------------


      3E- Enter message to be encrypted : ''')
print(''' 
    ''')

encrypted_text = ""

for letter in plain_text:
    
    com_letter = ord(letter)
    
    com_letter = (com_letter) + 1
    
    reverse = chr(com_letter)
    
    encrypted_text = encrypted_text + str(reverse)

print('''
      Your encrypted message is : ''',encrypted_text)  ; sleep(3)  

#Decryption Sevice
enter_encrypted_text = input('''


      3D- Enter message to be decrypted : ''')
print(''' 
    ''')

decrypted_text = ""

for char in enter_encrypted_text:
    
    com_char = ord(char)
    
    com_char = (com_char) - 1
    
    reverser = chr(com_char)
    
    decrypted_text = decrypted_text + str(reverser)
    
print('''
      Your decrypted message is : ''',decrypted_text) ; sleep(3)

#Footer


slowprint('''     -----------------------------------------------------
''')

slowprint('''       Disconnecting from server database-192.168.60.70...''') ; sleep(3)
slowprint('''       Database disconnected...''') ; sleep(2)
slowprint('''       Deleting encryption data...''') ; sleep(1.5)
slowprint('''       Deleting chat history...''') ; sleep(1)
slowprint('''       Restore flash memory...''') ; sleep(2)
slowprint('''       Removing file from C:\\Users\\Documents\\IFN--System...''') ; sleep(2)
slowprint('''       Prepare system-kill...''') ; sleep(1.5)
slowprint('''       Setting countdown...''') ; sleep(2)
slowprint('''       Restore from IFNS- DDR3...''') ; sleep(1)
slowprint('''     -------------------------------------''')
slowprint('''       *Process complete.''') ; sleep(3)
slowprint('''



                    WARNING: ALL DATA would be erased within 25 seconds. ⓒ MTU Technologies 2022
                    
                    ''')

sleep(25) #this window won't close for 25 seconds, enough to see the greeting
