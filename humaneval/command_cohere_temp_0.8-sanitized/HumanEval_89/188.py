def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted.append((char + 2) % 26)
            else:
                encrypted.append((char + 2) % 26 + 96)
        else:
            encrypted.append(char)
    return ''.join(encrypted)