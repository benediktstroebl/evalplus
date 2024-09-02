
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = alphabet.upper()
    counter = 0
    encrypted_word = ""
    for letter in s:
        if letter in alphabet:
            index = alphabet.find(letter)
            encrypted_word += alphabet[(index + 2) % 26]
        elif letter in upper_alphabet:
            index = upper_alphabet.find(letter)
            encrypted_word += upper_alphabet[(index + 2) % 26]
        else:
            encrypted_word += letter
    return encrypted_word

