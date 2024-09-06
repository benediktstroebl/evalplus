def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        offset = char[1] - char[0]
        new_char = char[0] + 2 * offset
        new_char = new_char if new_char in alphabet else new_char % 26 + alphabet[0]
        encrypted += new_char

    return encrypted