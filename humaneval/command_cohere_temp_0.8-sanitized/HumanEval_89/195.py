def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            offset = (alphabet.find(char) + 2) % 26
            encryptedChar = alphabet[offset:][:offset]
            encrypted = encrypted + encryptedChar
        else:
            encrypted = encrypted + char
    return encrypted