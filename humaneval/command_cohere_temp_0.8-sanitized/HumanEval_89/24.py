def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = ord(char) + 2 * (ord(char) // 2)
        encryptedchar = chr(offset % 26 + 97)
        encrypted += encryptedchar
    return encrypted