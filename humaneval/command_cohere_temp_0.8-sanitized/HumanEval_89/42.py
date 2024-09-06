def encrypt(s):
    encrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate = 2
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.find(char) - rotate:alphabet.find(char)]
            encrypted.append(char)
    return ''.join(encrypted)