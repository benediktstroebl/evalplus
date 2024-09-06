def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 2
    for char in s:
        # multiply the shift to the corresponding index and obtain the character from the shifted alphabet
        encrypted.append(alphabet[alphabet.index(char) * shift])
    return ''.join(encrypted)