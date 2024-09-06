def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        index = alphabet.find(char)
        next_index = (index + rotation) % len(alphabet)
        encrypted.append(alphabet[next_index])
    return ''.join(encrypted)