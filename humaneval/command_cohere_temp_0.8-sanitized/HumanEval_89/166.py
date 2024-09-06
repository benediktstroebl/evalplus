def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96 + shift
            encrypted.append(chr(offset + 96))
        else:
            encrypted.append(char)
    return ''.join(encrypted)