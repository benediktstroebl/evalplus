def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotates = 2
    for char in s:
        offset = ord(char) // rotates
        encryptedChar = chr(ord(alphabet[offset]) + ord(char) % rotates)
        encrypted += encryptedChar
    return encrypted