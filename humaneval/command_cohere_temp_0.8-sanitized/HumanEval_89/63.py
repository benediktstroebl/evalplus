def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - 97)
        encrypted += alphabet[index:] if index < len(alphabet) else alphabet[:index]

    return encrypted