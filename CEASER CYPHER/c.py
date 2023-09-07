print ("                                                                       ")
print ("                                                                       ")
print ("            #####################################################" )       
print ("            #                                                   #" )        
print ("            #                   Caesar Cipher tool              #" ) 
print ("            #                                                   #" )                          
print ("            #                   Cryptography Tool               #" )        
print ("            #                                                   #" )            
print ("            #                                                   #" )       
print ("            #                Author : Rinisha verma             #" )       
print ("            #                                                   #" )       
print ("            #####################################################" )       

print("                                                                   ")


print("                                           ")


def encrypt(message,shift):

    cypher_text=""
    for letter in message:
        if letter in alphabet:
         position=alphabet.index(letter)
         new_positon=position+shift
         new_letter=alphabet[new_positon]
         cypher_text+=new_letter
        else:
           cypher_text+=letter 
    print(f"The encoded cypher text is {cypher_text}")
def decrypt(message,shift):

    cypher_text=""
    for letter in message:
        if letter in alphabet:
         position=alphabet.index(letter)
         new_positon=position-shift
         new_letter=alphabet[new_positon]
         cypher_text+=new_letter
        else:
           cypher_text+=letter 
    print(f"The decoded cypher text is {cypher_text}")



 

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
flag=True
while flag:
    direction=input("Type 'encode' to encrypt OR type 'decode' to decrypt:")
    text=input("Type your message:").lower()
    shift=int(input("Enter the number of shifts:"))
    shift=shift%26

    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)
    result=input("Do you want to enter another message?")
    if result=="no":
        print("Good Bye!")
        flag=False
