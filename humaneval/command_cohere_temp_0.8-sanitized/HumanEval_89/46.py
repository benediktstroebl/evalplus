def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    for char in s:
      encrypted += rotated_alphabet[alphabet.find(char) + 2]
    return encrypted