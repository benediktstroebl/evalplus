def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        offset = (alphabet.find(char) + 2) // 2 * 2
        encrypted += alphabet[offset:] + alphabet[offset-2:offset]
    return encrypted