def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_by = 2 * 2

    for char in s:
        offset = ord(char) - 96
        encrypted_char = chr(offset + rotate_by)
        encrypted += encrypted_char

    return encrypted