# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice. Please choose E or D.")

if __name__ == "__main__":
    main()
