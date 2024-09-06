def encrypt(s):
    encrypted = []
    for letter in s:
        if letter.isalpha():
            offset = letter == 'z' or letter == 'Z'
            encrypted.append(chr((ord(letter) - 96 - offset) % 26 + 96 + offset))
        else:
            encrypted.append(letter)
    return ''.join(encrypted)