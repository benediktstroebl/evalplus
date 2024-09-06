def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotations = [alphabet[i:i+2] for i in range(0, 26, 2)]
    for char in s:
      encrypted += rotations[alphabet.find(char)]
    return encrypted