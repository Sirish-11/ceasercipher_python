"""start"""
import string
def welcome():
    """making first function"""
    print("Welcome to Caesar Cipher.")
    print("This program encrypt or decrypts text with the Caesar Cipher.")
def enter_message():
    """making second function which is the nost important function for this program"""
    userinput=input("Press E to encrpyt your message and D to decrypt your message: ")
    message =input("Enter the message you would like to encrypt or decrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    if userinput=="E" or userinput=="e":
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif userinput== "D" or userinput=="d":
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Your request is invalid")
def encrypt(message, shift):
    """a function to encrypt the message"""
    alphabet = string.ascii_uppercase
    encrypted_message = ""
    for hrikiss in message:
        if hrikiss.isalpha():
            idx = alphabet.index(hrikiss.upper())
            idx = (idx + shift) % 26
            encrypted_message += alphabet[idx]
        else:
            encrypted_message += hrikiss
    return encrypted_message
def decrypt(message, shift):
    """a function to decrypt the message"""
    alphabet = string.ascii_uppercase
    decrypted_message = ""
    for hrikiss in message:
        if hrikiss.isalpha():
            idx = alphabet.index(hrikiss.upper())
            idx = (idx - shift) % 26
            decrypted_message += alphabet[idx]
        else:
            decrypted_message += hrikiss
    return decrypted_message
def main():
    """calling both functions"""
    welcome()
    enter_message()
    userinputo=input("Do you want to run this program again? If no, type any key but y and if yes, type Y/y: ")
    if userinputo=="Y" or userinputo=="y":
        main()
    else:
        print("Thank you for using this program made by Hrikiss")
if __name__ == "__main__":
    main()
