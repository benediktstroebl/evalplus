def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 2
    for char in s:
        index = alphabet.find(char)
        next_index = (index + shift) % len(alphabet)
        encrypted.append(alphabet[next_index])
    return ''.join(encrypted)