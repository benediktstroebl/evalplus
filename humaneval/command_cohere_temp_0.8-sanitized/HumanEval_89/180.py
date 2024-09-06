def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # multiply char by 2, taking modulo 26
        char_double = (ord(char) * 2) % 26
        # add two to char double and take modulo 26
        char_double_shifted = (char_double + 2) % 26
        encrypted.append(alphabet[char_double_shifted])
    return ''.join(encrypted)