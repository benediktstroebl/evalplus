def encrypt(s):
    encrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96
            encrypt_offset = (offset + rotate) % 26
            encrypted.append(chr(encrypt_offset + 96))
        else:
            encrypted.append(char)
    return ''.join(encrypted)