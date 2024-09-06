def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = alphabet[2:] + alphabet[:2]
    for char in s:
      encrypted += rot_alphabet[alphabet.find(char)]
    return encrypted