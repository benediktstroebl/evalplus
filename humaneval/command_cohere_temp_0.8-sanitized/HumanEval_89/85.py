def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    for char in string:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += rotated_alphabet[index]
        else:
            encrypted += char
    return encrypted