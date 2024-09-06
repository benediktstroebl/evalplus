def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
      char_code = alphabet.find(char) + 2 * 2
      encryptedchar = alphabet[char_code % 26]
      encrypted += encryptedchar
    return encrypted