def encrypt(s):
    encrypted = []
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                encrypted.append((letter + 2) % 26 + 'A')
            else:
                encrypted.append((letter + 2) % 26 + 'a')
        else:
            encrypted.append(letter)
    return ''.join(encrypted)