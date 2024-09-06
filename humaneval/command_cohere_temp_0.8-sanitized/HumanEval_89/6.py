def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * 2
        if index > 26:
            index -= 26
        encrypted += alphabet[index]

    return encrypted