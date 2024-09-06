def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2]
    return encrypted