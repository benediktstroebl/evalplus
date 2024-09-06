def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotations = [None, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + rotations[index % 23]]
    
    return encrypted