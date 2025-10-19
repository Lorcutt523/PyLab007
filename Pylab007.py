alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
alpha_len = len(alphabet)
encrypted_texts = []
keys= []
key_index = 0

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    square = []

    for shift in range(alpha_len):
        row = [alphabet[(i + shift) % alpha_len] for i in range(alpha_len)]
        square.append(row)
    def cell(char):
        return f"{char:^3}|"

    header ="  " + "".join(cell(c) for c in alphabet)
    print(header)
    print("|   |" + "---|"* (alpha_len + 1))

    for i, row in enumerate(square):
        line = f"{alphabet[i]:^2} |"
        for c in row:
            line += f" {c:^3}|"
        print(line)
    return square

def pretty_print(vsq:list):
    for i, row in enumerate(vsq):
        print(f"| {'|   '.join(row)} |")
        if i == 0:
            suffix = ' --- |'*(alpha_len+1)
            print(f'|{suffix}')


# ENCRYPTION
def letter_to_index(letter, alphabet: str):
    return alphabet.index(letter)

def index_to_letter(index, alphabet):
    return alphabet[index % len(alphabet)]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_list = []
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char in alphabet:
            key_char = key[i % key_length]
            cipher_index = vigenere_index(key_char, char, alphabet)
            cipher_list.append(index_to_letter(cipher_index, alphabet))
        else:
            cipher_list.append(char)


    return ''.join(cipher_list)

# DECRYPTION
def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return (letter_to_index(cipher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % len(alphabet)

def decrypt_vigenere(key, ciphertext, alphabet):
    plain_text = []
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char in alphabet:
            key_char = key[i % key_length]
            plain_index = undo_vigenere_index(key_char, char, alphabet)
            plain_text.append(index_to_letter(plain_index, alphabet))
        else:
            plain_text.append(char)

    return "".join(plain_text)

# APP FUNCTIONS

def encrypt_menu():
    """Encrypts plaintext and stores"""
    global  key_index
    if not keys:
        print("No keys provided")
        return
    key = keys[key_index]
    plaintext = input("Plaintext: ")
    cipher = encrypt_vigenere(key, plaintext, alphabet)
    encrypted_texts.append(cipher)
    print(f"Encrypted and stored: {cipher}")
    key_index = (key_index + 1) % len(keys)

def decrypt_menu():
    """decrypt all stored messages"""
    if not encrypted_texts:
        print("No encrypted messages found")
        return
    if not keys:
        print("No keys found")
        return

    print("\n Decrypted messages:")
    for i, cipher  in enumerate(encrypted_texts):
        key = keys[i % len(keys)]
        plain = decrypt_vigenere(key, cipher, alphabet)
        print(f"{i+1}) Key {key}: {plain}")

def dump_encrypted():
    """print all  stored encrypted messages"""
    if not encrypted_texts:
        print("No encrypted messages found")
        return
    print("\n Encrypted messages:")
    for i, cipher in enumerate(encrypted_texts, start=1):
        print(f"{i}) {cipher}")

def add_keys():
    """Add multiple keys"""
    global keys, key_index
    keys_input = input("Enter your key(s) separated by commas: ")

    keys = []
    for k in keys_input.split(','):
        if k.strip():
            keys.append(k.strip())
    key_index = 0
    print(f" Loaded {len(keys)} keys: {keys}")

def quit_app():
    print("Goodbye!")
    exit()

#menu

menu = [
    ["Encrypt", encrypt_menu],
    ["Decrypt", decrypt_menu],
    ["Show Vigenere Square", vigenere_sq],
    ["Dump  Encrypted Texts", dump_encrypted],
    ["Add Keys", add_keys],
    ["Quit", quit_app]

]

def main():
    print("VIGENERE CIPHER APP")

    while True:
        print("\nMenu:")
        for i, item in enumerate(menu, start=1):
            print(f"{i}) {item[0]}")

        choice = input("Choose an option: ")

        if choice.isdigit() and 1 <= int(choice) <= len(menu):
            func = menu[int(choice) - 1][1]
            if func:
                if func == vigenere_sq:
                    func(alphabet)
                else:
                    func()
            else:
                print("No function assigned.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()










