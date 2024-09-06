def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_by = 2 * 2

    for char in s:
        if char.isalpha():
            offset = ord(char) - ord('a')
            encryptedChar = chr(ord('a') + (offset + rotate_by) % 26)
        else:
            encryptedChar = char
        encrypted += encryptedChar

    return encrypted