def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_idx = 2
    for char in s:
        encrypted_char = alphabet[alphabet.find(char) + rot_idx]
        encrypted = encrypted + encrypted_char
    return encrypted