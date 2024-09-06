def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - ord('a') + 1)
        encryptedChar = alphabet[index % 26]
        encrypted += encryptedChar

    return encrypted