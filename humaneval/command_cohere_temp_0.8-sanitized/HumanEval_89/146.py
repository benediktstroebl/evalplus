def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                offset = ord('Z') - ord('A')
                char_code = (ord(char) - ord('A') + 2) % offset * 2 + ord('A')
                encrypted.append(chr(char_code))
            else:
                offset = ord('z') - ord('a')
                char_code = (ord(char) - ord('a') + 2) % offset * 2 + ord('a')
                encrypted.append(chr(char_code))
        else:
            encrypted.append(char)
    return ''.join(encrypted)