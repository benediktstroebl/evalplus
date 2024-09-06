def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in string:
      char_index = alphabet.find(char)
      shifted_char_index = (char_index + 2) % len(alphabet)
      encrypted.append(alphabet[shifted_char_index])
    return ''.join(encrypted)