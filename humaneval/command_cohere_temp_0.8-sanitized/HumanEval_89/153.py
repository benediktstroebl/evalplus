def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
        encrypted.append(alphabet[index + 2 * (index % 2) :: 2])
    return ''.join(encrypted)