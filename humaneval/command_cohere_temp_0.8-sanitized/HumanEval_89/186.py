def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96 + rotation // 2
            encrypted.append(chr(offset + 96))
        else:
            encrypted.append(char)
    return "".join(encrypted)