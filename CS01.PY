# Updated Caesar Cipher Program with clearer result output

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher ===")
    choice = input("Encrypt or Decrypt? (E/D): ").strip().upper()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        encrypted = caesar_cipher(message, shift)
        print("Result: The encrypted message is →", encrypted)
    elif choice == 'D':
        decrypted = caesar_cipher(message, -shift)
        print("Result: The decrypted message is →", decrypted)
    else:
        print("Invalid option. Choose E or D.")

if __name__ == "__main__":
    main()
