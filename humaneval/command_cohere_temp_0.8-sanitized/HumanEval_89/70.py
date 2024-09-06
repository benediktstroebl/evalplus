def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = alphabet[2::2] + alphabet[1::2] + alphabet[0::2]
    for char in s:
      encrypted.append(rotated_alphabet[alphabet.index(char)])
    return ''.join(encrypted)