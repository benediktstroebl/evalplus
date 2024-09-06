def encrypt(s):
    encrypted = ''
    rotating_letters = 'abcdefghijklmnopqrstuvwxyz'
    offset = 2
    for char in s:
        offset_pos = char.isalpha() + char.lower() - 97 - offset
        encrypted_char = rotating_letters[offset_pos % 26]
        encrypted += encrypted_char
    return encrypted