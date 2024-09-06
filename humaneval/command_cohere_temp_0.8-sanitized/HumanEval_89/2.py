def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        index = alphabet.find(letter)
        encrypted.append(alphabet[index+2])
    return ''.join(encrypted)