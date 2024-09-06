def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_alphabet = alphabet[2:] + alphabet[:2]

    for char in string:
        if char.isalpha():
            char = char.lower()
            encrypted_index = alphabet.find(char) + 2
            encrypted_char = encrypted_alphabet[encrypted_index]
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted