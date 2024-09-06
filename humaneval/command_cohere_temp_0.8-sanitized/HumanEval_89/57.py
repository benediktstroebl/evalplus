def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * (index > alphabet.index('z') or index < alphabet.index('a'))]

    return encrypted