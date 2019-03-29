import time
import random

words = ['HELLO', 'CHECK', 'START', 'CINEMA', 'READY', 'EXAMPLE']
keys = ['WORLD', 'LOOK', 'FOR', 'WHERE', 'WHAT', 'NEED']

arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print()

def switch(n):
    print('''In a Caesar cipher, 
each letter of the alphabet 
is shifted along some number 
of places. For example, in a 
Caesar cipher of shift 
3, A would become D, B would become 
E, Y would become B and so on. The 
Vigenère cipher has several Caesar
ciphers in sequence with different shift values.
To encrypt, a table of alphabets 
can be used, termed a tabula recta,
Vigenère square or Vigenère 
table. It has the alphabet written 
out 26 times in different rows, each alphabet shifted cyclically 
to the left compared to the previous alphabet, corresponding to the 26 possible 
Caesar ciphers. At different points in the encryption process, the cipher 
uses a different alphabet from one of the rows. 
The alphabet used at each point depends on a repeating keyword''')
    print()
    while n < 26:
        for i in arr:
            if i==arr[0]:
                print(end='|')
            print(i, end='|')
        arr.append(arr[0])
        arr.remove(arr[0])
        print()
        n += 1
        print()


def start():
    m = random.choice(words)
    k = words.index(m)
    word = words[k]
    wordkey = keys[k]

    wordkey *= len(word) // len(wordkey) + 1
    c = ''
    # ENCODE
    for i, j in enumerate(word):
        gg = (ord(j) + ord(wordkey[i]))
        c += chr(gg % 26 + 65)
    answer = ''
    while answer != word:
        print("WORD-KEY => " + '[' + wordkey + ']\n')
        print("WORD =====> " + '[' + str(c) + ']\n')
        answer = input('\n Write correct word\n')
        if answer.lower() == word.lower():
            print('CORRECT!!')
            function()
        else:
            print("UNCORRECT! TRY AGAIN\n")


print("Hello")
def function():
    choice = input("Are you ready? y = START, n = DESCRIPTION [y / n] \n")
    if choice.lower() == 'y':
        start()
    elif choice.lower() == 'n':
        switch(0)
    else:
        print("UNCORRECT")


function()
