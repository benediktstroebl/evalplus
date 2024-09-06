def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply char by -2 and convert to char
        encrypted.append(alphabet[int(char) * -2])
    return ''.join(encrypted)