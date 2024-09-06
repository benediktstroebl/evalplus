def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char)
        delta = (index + 2) // 2 * 2
        encrypted += alphabet[index + delta]

    return encrypted