def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_letters = 2 * 2
    for letter in s:
        encrypted_letter = alphabet[alphabet.find(letter) + rotate_letters]
        encrypted += encrypted_letter
    return encrypted