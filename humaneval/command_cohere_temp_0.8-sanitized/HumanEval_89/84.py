def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2]

    return encrypted