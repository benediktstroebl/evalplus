def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        if char in alphabet:
            idx = alphabet.find(char)
            encrypted.append(alphabet[(idx + rotation) % len(alphabet)])
        else:
            encrypted.append(char)
    return ''.join(encrypted)