def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                offset = ord('Z') - ord('A')
                encrypted.append(chr((ord(char) - offset + 2) % 26 + ord('A')))
            else:
                offset = ord('z') - ord('a')
                encrypted.append(chr((ord(char) - offset + 2) % 26 + ord('a')))
        else:
            encrypted.append(char)
    return ''.join(encrypted)