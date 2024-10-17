def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text += encrypted_char
        elif char.isdigit():
            encrypted_char = chr(((ord(char) - 48 + shift) % 10) + 48)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        elif char.isdigit():
            decrypted_char = chr(((ord(char) - 48 - shift) % 10) + 48)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def get_shift_value():
    while True:
        try:
            shift = int(input("Enter the shift value (positive or negative integer): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

def main():
    while True:
        print("Advanced Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = get_shift_value()
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}\n")
            
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = get_shift_value()
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}\n")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
