import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters


chars = list(chars)
key = chars.copy()


random.shuffle(key)

print("Original characters:", chars)
print("Shuffled key:", key)


def encrypt(plain_text):
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  
    return cipher_text

def decrypt(cipher_text):
    decrypted_text = ""

    decryption_map = {key[i]: chars[i] for i in range(len(chars))}

    for letter in cipher_text:
        if letter in decryption_map:
            decrypted_text += decryption_map[letter]
        else:
            decrypted_text += letter  
    return decrypted_text


while True:
    print("\nOptions:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        plain_text = input("Enter a message to encrypt: ")
        cipher_text = encrypt(plain_text)
        print("Cipher text:", cipher_text)

    elif choice == '2':
        cipher_text = input("Enter a message to decrypt: ")
        decrypted_text = decrypt(cipher_text)
        print("Decrypted text:", decrypted_text)

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
