def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate = 2
    for char in s:
      if char.isalpha():
        char = alphabet[alphabet.index(char) - rotate:alphabet.index(char) + rotate + 26]
        encrypted.append(char)
    return ''.join(encrypted)