def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = char[1] - char[0]
        encrypt_char = chr(ord(char[0]) + offset)
        encrypted = f"{encrypt_char}{encrypted}"
    return encrypted