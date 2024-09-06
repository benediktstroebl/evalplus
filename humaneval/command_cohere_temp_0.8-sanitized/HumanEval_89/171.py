def encrypt(s):
    encrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96
            encrypted.append(chr(offset + rotation * 2))
        else:
            encrypted.append(char)
    return ''.join(encrypted)