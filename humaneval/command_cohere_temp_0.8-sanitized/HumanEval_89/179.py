def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_letters = 2 * 2
    for letter in s:
        # Find the letter's index in the English alphabet
        index = alphabet.find(letter)
        # Add the letter from the rotated position
        encrypted += alphabet[index + rotate_letters]
    return encrypted