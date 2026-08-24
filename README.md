#  Simple Encryption & Decryption Tool

A beginner-friendly **Python cybersecurity project** that demonstrates how encryption can protect sensitive messages.

The project allows a user to:

*  Encrypt a message using a secret password
*  Decrypt the encrypted message using the same password
*  Convert the password into a secure encryption key using PBKDF2
*  Store encrypted data in a file
*  Detect an incorrect password during decryption

---

##  Project Overview

When a normal text message is stored in a file, anyone who can access the file may be able to read it.

For example:

```text
Hello Amandeep
```

This project converts the readable message into encrypted data:

```text
gAAAAAB...
```

The original message can only be recovered using the correct secret password.

### Basic workflow

```text
                 User Password
                       |
                       v
              +----------------+
              |     PBKDF2     |
              | Key Derivation |
              +-------+--------+
                      |
                      v
                Fernet Key
                      |
          +-----------+-----------+
          |                       |
          v                       v
      Encryption              Decryption
          |                       ^
          v                       |
   Encrypted Message      Secret Password
          |
          v
encrypted_message.txt
```

---

##  Objectives

The main objectives of this project are:

1. Understand the basic concept of encryption.
2. Learn how symmetric encryption works.
3. Understand the role of a secret password.
4. Learn how passwords can be converted into encryption keys.
5. Encrypt and decrypt messages using Python.
6. Understand the importance of protecting encryption keys.
7. Practice Python file handling and exception handling.

---

##  Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python 3     | Programming language                |
| Cryptography | Encryption library                  |
| Fernet       | Symmetric authenticated encryption  |
| PBKDF2HMAC   | Password-based key derivation       |
| SHA-256      | Hashing algorithm used by PBKDF2    |
| Git/GitHub   | Version control and project hosting |
| Kali Linux   | Testing environment                 |

---

##  Project Structure

```text
Simple-Encryption-Tool/
│
├── encryption_tool.py
├── encrypted_message.txt
├── salt.bin
├── .gitignore
└── README.md
```

### File description

#### `encryption_tool.py`

Main Python program responsible for:

* Taking the user's password
* Creating an encryption key
* Encrypting messages
* Decrypting messages
* Handling incorrect passwords

#### `encrypted_message.txt`

Stores the encrypted message.

Example:

```text
gAAAAAB...
```

The original readable message is not stored directly.

#### `salt.bin`

Stores the random salt used by PBKDF2 during key derivation.

The salt is not a secret password, but it must be preserved to derive the same key later.

#### `.gitignore`

Prevents sensitive/generated files from being uploaded to GitHub.

Example:

```text
encrypted_message.txt
salt.bin
__pycache__/
*.pyc
```

---

#  How the Encryption Works

The project uses **symmetric encryption**.

Symmetric encryption means the same derived key is used to encrypt and decrypt the data.

The process is:

```text
User Password
      |
      v
     Salt
      |
      v
PBKDF2HMAC + SHA-256
      |
      v
Fernet Encryption Key
      |
      +--------------------+
      |                    |
      v                    v
   Encrypt              Decrypt
      |                    ^
      v                    |
Encrypted Data       Same Password
```

---

##  Step 1 — User Creates a Password

When the program starts, it asks:

```text
Enter your secret password:
```

For example:

```text
MySecret123
```

The password is not directly used as the Fernet key.

Instead, it is converted into a suitable encryption key.

---

##  Step 2 — Generate a Salt

The program creates a random salt:

```python
salt = os.urandom(16)
```

The salt is saved in:

```text
salt.bin
```

The salt helps make password-derived keys more resistant to precomputed attacks.

---

##  Step 3 — Generate the Encryption Key

The project uses:

```python
PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=600000
)
```

The user's password and salt are processed by PBKDF2.

The result is converted into a Fernet-compatible key.

Conceptually:

```text
Password + Salt
      |
      v
    PBKDF2
      |
      v
Encryption Key
```

---

#  Step 4 — Encrypt the Message

Suppose the user enters:

```text
Hello Amandeep
```

The program uses Fernet:

```python
cipher = Fernet(key)
encrypted = cipher.encrypt(message.encode())
```

The result may look like:

```text
gAAAAABp...
```

This encrypted data is stored in:

```text
encrypted_message.txt
```

---

#  Step 5 — Decrypt the Message

When the user chooses:

```text
2. Decrypt Message
```

the program reads:

```text
encrypted_message.txt
```

It derives the encryption key from the entered password and the saved salt.

Then:

```python
decrypted = cipher.decrypt(encrypted)
```

The original message is recovered:

```text
Hello Amandeep
```

---

#  Wrong Password Test

Suppose the original password is:

```text
MySecret123
```

The message is encrypted using that password.

If someone enters:

```text
WrongPassword
```

during decryption, the derived key will be different.

The program displays:

```text
Decryption failed!
Wrong secret password or corrupted file.
```

This demonstrates the importance of the secret password.

---

#  Installation

## 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project:

```bash
cd Simple-Encryption-Tool
```

---

## 2. Install the dependency

```bash
pip3 install cryptography
```

On Kali Linux, if the package is already installed, you may see:

```text
Requirement already satisfied: cryptography
```

This means the library is already available.

---

#  Running the Project

Run:

```bash
python3 encryption_tool.py
```

The program displays:

```text
===== Simple Encryption Tool =====

Enter your secret password:

===== MENU =====
1. Encrypt Message
2. Decrypt Message
3. Exit

Enter your choice:
```

---

#  Example

## Encryption

Select:

```text
1
```

Enter:

```text
Hello Amandeep
```

Output:

```text
Message encrypted successfully!

Encrypted data:
gAAAAAB...
```

The encrypted message is stored in:

```text
encrypted_message.txt
```

---

## Decryption

Select:

```text
2
```

Enter the same password.

Output:

```text
Decrypted message:
Hello Amandeep
```

---

#  Important Concepts Learned

### 1. Encryption

Encryption converts readable data into unreadable data.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
```

### 2. Decryption

Decryption converts ciphertext back into the original message.

```text
Ciphertext
   ↓
Decryption
   ↓
Plaintext
```

### 3. Symmetric Encryption

The same encryption key is used for encryption and decryption.

```text
             Same Key
                |
        +-------+-------+
        |               |
        v               v
    Encryption      Decryption
        |               |
        v               ^
    Ciphertext ------> Plaintext
```

### 4. Password-Based Key Derivation

PBKDF2 converts a password into a cryptographic key suitable for encryption.

```text
Password
   +
Salt
   ↓
PBKDF2
   ↓
Encryption Key
```

---

# Security Considerations

This project is intended for **learning and demonstration purposes**.

Important security practices:

* Never share your secret password.
* Never upload real encryption keys to GitHub.
* Do not commit sensitive encrypted data containing real information.
* Keep `salt.bin` available for decrypting existing messages.
* Use a strong password.
* Do not use this simple project as a production password manager or secure messaging application without additional security controls.

---

#  Project Architecture

```text
+----------------------+
|        User          |
+----------+-----------+
           |
           | Password
           v
+----------------------+
|     PBKDF2HMAC       |
|      SHA-256         |
+----------+-----------+
           |
           | Derived Key
           v
+----------------------+
|       Fernet         |
| Symmetric Encryption |
+----------+-----------+
           |
       +---+---+
       |       |
       v       v
  Encryption  Decryption
       |       |
       v       ^
+----------------------+
| encrypted_message   |
|       .txt           |
+----------------------+

        salt.bin
           |
           v
      PBKDF2HMAC
```

---

#  Complete Workflow

```text
              START
                |
                v
       Enter Secret Password
                |
                v
          Read/Create Salt
                |
                v
        Derive Fernet Key
                |
                v
          Display Menu
                |
        +-------+-------+
        |               |
        v               v
    Encrypt          Decrypt
        |               |
        v               v
   Enter Message    Read File
        |               |
        v               v
     Encrypt       Decrypt Using
        |            Derived Key
        v               |
 Save Encrypted         v
    Message        Show Original
        |               |
        +-------+-------+
                |
                v
               EXIT
```

---

#  Future Improvements

Possible improvements for the next version:

* Encrypt complete files instead of only messages.
* Add a graphical user interface.
* Add password confirmation.
* Add password strength checking.
* Allow multiple encrypted messages.
* Add secure file deletion.
* Add logging of encryption/decryption operations.
* Add unit tests.
* Add a command-line interface using `argparse`.
* Add support for encrypted PDF/text files.

---

#  Learning Outcome

After completing this project, you should understand:

```text
Password
   ↓
Salt
   ↓
PBKDF2
   ↓
Encryption Key
   ↓
Fernet
   ↓
Encrypted Message
   ↓
Fernet + Correct Key
   ↓
Original Message
```

This project provides a simple practical introduction to **cryptography, symmetric encryption, password-based key derivation, Python file handling, and basic cybersecurity concepts**.

---

##  Author

**Amandeep Singh**

Cybersecurity / SOC Analyst Learning Project

---

##  Disclaimer

This project is created for **educational and cybersecurity learning purposes**. It should not be considered a production-ready secure messaging or data-protection solution.
