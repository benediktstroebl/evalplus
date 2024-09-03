def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[(index + 2) % 26]

    return encrypted