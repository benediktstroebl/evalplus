def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + 2*(ord(char) // 2)]
        encrypted += char
    return encrypted