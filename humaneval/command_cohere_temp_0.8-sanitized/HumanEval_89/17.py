def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = ord(char) + 2 * (ord(char) // 2)
        encryptedChar = chr(offset % 26 + 97)
        encrypted += encryptedChar
    return encrypted