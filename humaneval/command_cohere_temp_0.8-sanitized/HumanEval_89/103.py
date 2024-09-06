def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
      char_code = alphabet.find(char) + 2 * 2
      encrypted += alphabet[char_code % 26]
    return encrypted