def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 2
    for char in s:
        if char.isalpha():
            offset = alphabet.find(char)
            encrypted.append(alphabet[offset+shift])
        else:
            encrypted.append(char)
    return ''.join(encrypted)