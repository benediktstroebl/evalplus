def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate_map = str.maketrans(alphabet, alphabet[2:] + alphabet[:2])
    for char in s:
      encrypted.append(char.translate(rotate_map))
    return ''.join(encrypted)