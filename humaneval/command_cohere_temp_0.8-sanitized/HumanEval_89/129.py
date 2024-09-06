def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_letters = 2
    for char in s:
        encrypted_char = alphabet[(alphabet.find(char) + rotate_letters) % 26]
        encrypted += encrypted_char
    return encrypted