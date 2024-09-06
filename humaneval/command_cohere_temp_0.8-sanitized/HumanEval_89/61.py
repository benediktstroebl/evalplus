def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alphabet = alphabet[2::2] + alphabet[1::2]
    for char in s:
      if char in alphabet:
        encrypted.append(rotated_alphabet[alphabet.index(char)])
      else:
        encrypted.append(char)
    return ''.join(encrypted)