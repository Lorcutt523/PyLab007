alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
#my_list = [[][][]]

def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print("|   | " + " | ".join(alphabet) + " |")
    print("|---|" + "|".join(["---"] * alpha_len) + "|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
       row = [alphabet[(i + shift) % alpha_len] for i in range(alpha_len)]
    print(f"|{alphabet[shift]}| " + " | ".join(row) + " |")


def letter_to_index(letter, alphabet: str):
    return alphabet.lower().index(letter.lower())

def index_to_letter(index, alphabet):
    return alphabet[index % len(alphabet)]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    key = key.upper()
    plaintext = plaintext.upper()
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif c in alphabet:
            key_letter = key[counter%len(key)]
            cipher_index = vigenere_index(key_letter, c, alphabet)
            cipher_letter = index_to_letter(cipher_index, alphabet)
            cipher_text += cipher_letter
            counter += 1
        else:
            cipher_text += c
    return cipher_text

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return (letter_to_index(cipher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % len(alphabet)

def decrypt_vigenere(key, ciphertext, alphabet):
    plain_text = ''
    key = key.upper()
    ciphertext = ciphertext.upper()
    counter = 0

    for c in ciphertext:
        if c == ' ':
            plain_text += ' '
        elif c in alphabet:
            key_letter = key[counter%len(key)]
            plain_index = undo_vigenere_index(key_letter, c, alphabet)
            plain_letter = index_to_letter(plain_index, alphabet)
            plain_text += plain_letter
            counter += 1
        else:
            plain_text += c
    return plain_text




key = 'DAVINCI'
plaintext = 'THE EAGLE HAS LANDED'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#(vigenere_sq(alphabet))
#print(letter_to_index('H', alphabet))
#print(index_to_letter(7, alphabet))
#(index_to_letter(vigenere_index('B', 'H', alphabet), alphabet))
#print(encrypt_vigenere('DAVINCI', 'THE EAGLE HAS LANDED', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

cipher = encrypt_vigenere(key, plaintext, alphabet)
#print("encrypted: ", cipher)

decrypt_vigenere(key, cipher, alphabet)
#print("decrypted: ", decrypted)


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        print("Vigenere Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print('3 Show Vigenere Square')
        print('4. Exit')
        choice = input("choose an option:")
        if choice == '1':
            key = input("Enter the key:").upper()
            text = input("Enter plaintext:")
            print("Encrypted: " + encrypt_vigenere(key, text, alphabet))

        elif choice == '2':
            key = input("Enter key:").upper()
            text = input("Enter ciphertext:")
            print("Decrypted: " + decrypt_vigenere(key, text, alphabet))

        elif choice == '3':
            vigenere_sq(alphabet)

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Wrong Choice")
if __name__ == '__main__':
            main()


#def pretty_print(vsq:list):
    #for i, row in enumerate(vsq)
        #print(f"| {' | '.join(row)} |")
        #if i == 0:
            #suffix = '---|'*(aplha_len+1)
            #print(f'|{suffix}')
