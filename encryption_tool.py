from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"
MESSAGE_FILE = "encrypted_message.txt"


# Step 1: Generate or load encryption key
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


# Step 2: Encrypt the message
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())

    with open(MESSAGE_FILE, "wb") as file:
        file.write(encrypted)

    return encrypted


# Step 3: Decrypt the message
def decrypt_message(key):
    if not os.path.exists(MESSAGE_FILE):
        print("No encrypted message found.")
        return

    with open(MESSAGE_FILE, "rb") as file:
        encrypted = file.read()

    cipher = Fernet(key)

    try:
        decrypted = cipher.decrypt(encrypted)
        print("\nDecrypted message:")
        print(decrypted.decode())

    except Exception:
        print("\nDecryption failed!")
        print("The key may be incorrect or the file may be damaged.")


# Main program
key = load_key()

while True:
    print("\n===== Simple Encryption Tool =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        message = input("Enter message: ")

        encrypted = encrypt_message(message, key)

        print("\nMessage encrypted successfully!")
        print("Encrypted data:")
        print(encrypted.decode())

    elif choice == "2":
        decrypt_message(key)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
