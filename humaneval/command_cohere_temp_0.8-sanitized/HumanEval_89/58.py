def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply char by -2 and convert to char
        char_two = ord(char) * -2
        char_two = chr(char_two)
        # If char_two is not in alphabet, convert to char in alphabet
        if char_two not in alphabet:
            char_two = chr(ord('a') + ord(char_two) - 96)
        encrypted.append(char_two)
    return ''.join(encrypted)