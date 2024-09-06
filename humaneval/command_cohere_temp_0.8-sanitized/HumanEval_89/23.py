def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        if index == -1:
            encrypted += char
        else:
            encrypted += alphabet[index + 2 * (alphabet[index::2] == char)]

    return encrypted