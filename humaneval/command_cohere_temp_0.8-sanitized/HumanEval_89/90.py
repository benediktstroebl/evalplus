def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply character code by 2 and rotate the alphabet
        char_code = ord(char) * 2
        rotated_char = alphabet[char_code - 96]
        encrypted.append(rotated_char)
    return ''.join(encrypted)