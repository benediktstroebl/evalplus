def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply char by -2 and convert to char
        char_index = alphabet.find(char) - 2
        while char_index < 0:
            char_index += 26
        encrypted.append(alphabet[char_index])
    return ''.join(encrypted)