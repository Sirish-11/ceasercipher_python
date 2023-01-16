import string 
print("Welcome to the Casear Cipher\nThis program encrypts and decrypts text using Caesar Cipher.")
def userinput():
    i = input("Would you like to encrypt (e) or decrypt(d)")
    if(i != "e" and i !="d"):
         print("Invalid code please re enter")
         i = input("Would you like to encrypt (e) or decrypt(d)")
    if(i == "e" ):
      m = input("What message would you like to encrypt : ")
      n = int(input("What is the shift number( enter the value between (1 to 25) : "))
      encrypted_message = encrypt(m,n)
      print("Encrypted message is",encrypted_message)  
    if i == "d":
        m = input("What message would you like to decrypt : ")
        n = int(input("What is the shift number( enter the value between (1 to 25) : "))
        decrypted_message = decrypt(m,n)
        print("Decrypted code is : ",decrypted_message)
def encrypt(m,n):
    formatting =string.ascii_uppercase
    encrypted_message = ""
    for char in m:
        if char.isalpha():
            v = formatting.index(char.upper())
            v = (v + n) % 26
            encrypted_message += formatting[v]
        else:
            encrypted_message += char
    return encrypted_message
def decrypt(m,n):
    formatting =string.ascii_uppercase
    decrypted_message = ""
    for char in m:
        formatting = string.ascii_uppercase
    decrypted_message = ""
    for char in m:
        if char.isalpha():
            v = formatting.index(char.upper())
            v = (v - n) % 26
            decrypted_message += formatting[v]
        else:
            decrypted_message += char
    return decrypted_message
def main():
    userinput()
    re_enter=input("Do you want to run this program again(y/n)? ")
    if re_enter =="y" or re_enter == "Y":
     main()
    else:
        print("Thank you for using this program")
if __name__ == "__main__":
    main()

Try this
