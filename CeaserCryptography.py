
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("That Is Not A Choice")


def encryption():
    print("Encryption")
    msg = input("Enter Your Message: ")
    key = int(input("Enter Key (1-94):"))

    encrypted_text = ""

    for i in range(len(msg)):
        temp = (ord(msg[i])+key)
        if (temp>126):
            temp = temp-127+32
        
        encrypted_text+=chr(temp)
    print("Encrypted: "+encrypted_text)
    main()

def decryption():
    print("Decryption")
    print("Message can only be lower or uppercase")
    encrypt_message = input("Enter Encrypted Text: ")
    decrypt_key = int(input("Enter Key (1-94):"))

    decrypted_text = ""
    for i in range (len(encrypt_message)):
        temp = (ord(encrypt_message[i])-decrypt_key)
        if (temp<32):
            temp = temp+127-32

        decrypted_text+=chr(temp)
    print("Decrypted Text: "+decrypted_text)
   

if __name__ == "__main__":
    main()
