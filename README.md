
## Caesar Cipher

### Description
The Enhanced Caesar Cipher is a Python application that allows users to encrypt and decrypt messages using a modified version of the traditional Caesar Cipher algorithm. This tool not only supports basic shift functionality but also incorporates advanced features like case sensitivity and punctuation handling, making it a robust option for secure text communication.

### Overview
The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. This project expands on that concept by allowing for customizable shifts, case-sensitive letters, and the ability to ignore non-alphabetical characters, enhancing the encryption's security and versatility.

### Features
- Customizable Shift: Users can define how many positions to shift each letter.
- Case Sensitivity: Maintains the original case of letters during encryption and decryption.
- Punctuation Handling: Ignores non-alphabetical characters during the shifting process.
- Multi-step Encryption: Supports applying multiple shifts for layered security.

### Installation
#### Prerequisites
- Python 3.x

#### Running the Application
Clone the repository or download the source code.

Ensure that Python is installed on your system.

Run the following command in your terminal to start the application:
```bash
python caesar_cipher.py
```

### How to Use
1. **Start the Application**: Run the script to launch the Caesar Cipher application.
2. **Input Message**: Enter the message you wish to encrypt or decrypt.
3. **Set Shift Value**: Specify the number of positions to shift the letters.
4. **Encrypt/Decrypt**: Choose the appropriate option to perform the desired operation.

### Key Components
- **Shift Calculation**: Logic for calculating the new letter position based on the input shift value.
- **Encryption and Decryption Functions**: Functions to handle the respective processes while maintaining text integrity.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

---
