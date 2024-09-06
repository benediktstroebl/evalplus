def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        offset = char[1] - char[0]
        num = ord(char[0]) + 97 if char[0] in alphabet and char[0] != 'a' else 97
        encryptedChar = chr(num + offset * 2)
        encryptedChar = chr(num + offset * 2 - 26) if encryptedChar in alphabet[:26] else chr(num + offset * 2 + 26)
        encrypted += encryptedChar
    return encrypted