def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted.append((char + 2) % 26 + 'A')
            else:
                encrypted.append((char + 2) % 26 + 'a')
        else:
            encrypted.append(char)
    return ''.join(encrypted)