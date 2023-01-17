import string 
print("Welcome to the Casear Cipher\nThis program encrypts and decrypts text using Caesar Cipher.")
def userinput():
    i = input("Would you like to encrypt (e) or decrypt(d)")
    if(i != "e" and i !="d"):
        while (i != "e" and i !="d"):
         print("Invalid code please re enter")
         i = input("Would you like to encrypt (e) or decrypt(d)")
         while(i == "e" and i =="d") :
            break
        return i 
    if(i == "e" ):
      m = input("What message would you like to encrypt : ")
      n = int(input("What is the shift number( enter the value between (1 to 25) : "))
      encrypted_message = encrypt(m, n)
      cap = encrypted_message
      g = cap.upper()
      print("encrypted code is:",g)  
    if i == "d":
        m = input("What message would you like to decrypt : ")
        n = int(input("What is the shift number( enter the value between (1 to 25) : "))
        decrypted_message = decrypt(m,n)
        print("Decrypted code is : ",decrypted_message)
def encrypt(m,s):
    formatting =string.ascii_uppercase
    encrypted_message = ""
    for char in m:
       if char.isalpha():
            shift = ord(char) + s
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26
                encrypted_message += chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('a'):
                    shift += 26
                encrypted_message += chr(shift)
    else:
        encrypted_message += char
    return encrypted_message
def decrypt(m,s):
    formatting =string.ascii_uppercase
    decrypted_message =""
    for char in m:
        if char.isalpha():
            idx = formatting.index(char.upper())
            idx = (idx - s) % 26
            decrypted_message += formatting[idx]
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
