# THE ARRAY OF CHARACTERS TO ENCODE
arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# SECOND ARRAY which equals arr1
arr2 = []
for i in range(len(arr1)):
    arr2.append(arr1[i])

# ENCODE/DECODE
def crypt_decrypt():
    for i in range(key):
        arr2.append(arr2[0])
        arr2.remove(arr2[0])

# CHOOSE type for encode
print('[ 1 ] => Crypt the text/file')
print('[ 2 ] => Decrypt text from the file')
print('[ 3 ] => Decrypt text from the terminal')

# write text and save in directory
try:
    choice = int(input("Write the number: \n [CHOICE] >> ")) # Choice
    if choice == 1:
        key = int(input("Write the key to encode \n [KEY] >> ")) # Key for encode
        crypt_decrypt()
        text = input('\n Write the text: \n[TEXT] >> ') # Text for encode
# Encoding process
        textcode = ''
        for i in text:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    textcode+=arr2[j]
        print("Crypred TEXT >> " + textcode)
# Save in file
        file = input('Write correct name for file\n Example =>[ text.txt ]  \n')
        crypt = open(file, 'w')
        crypt.write(textcode)
        crypt.close()
        input("press ENTER to exit")
    if choice == 2:
        key = int(input("Write the key: \n [KEY] >> "))
        crypt_decrypt()
        file = input('Write name file: \n [FILE] >> ')
        filed = open(file, 'r')
        read = filed.read()
        textd = ''
        for i in read:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    textd += arr1[j]
        print("\n Decrypt text: ")
        print(str(textd))
        answer = input('\n Save decrypted text in the file? [y / n] >> ')
        if answer == 'y' or answer == 'Y':
            file = input("Write file name \n [FILE] >> ")
            filew = open(file, 'w')
            filew.write(textd)
            filew.close()
            print('\n File '+file+' successfully saved!')
            input('press ENTER to exit')
        else:
            pass
        filed.close()
    if choice == 3:
        key = int(input("Write the key \n [KEY] >> "))
        crypt_decrypt()

        text = input('\n Write the crypted text: \n [TEXT] >> ')
        textd = ''
        for i in text:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    textd += arr1[j]
        print('\n Decrypted text: \n [TEXT] >> ')
        print(str(textd))
        input('press ENTER to exit')
    else:
        print("Number is not defined!")
except ValueError:
    print("ERROR! Only Integer Numbers!")