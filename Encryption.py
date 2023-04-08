# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

choice=int(input("Enter 1 for code and 2 for decode: "))
msg=input("Enter Your Message: ")
if choice==1:
     if len(msg)<3:
         print(msg[::-1])
     else:
         str=msg[1:len(msg)]
         print(random.choice(b)+random.choice(b)+random.choice(b)+str+msg[0]+random.choice(b)+random.choice(b)+random.choice(b))
else:
    if len(msg) < 3:
        print(msg[::-1])
    else:
        str2= msg[3:len(msg)-4]
        print(msg[len(msg)-4]+str2)
