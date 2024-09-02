
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
    new_alphabet = []
    for letter in alphabet:
        if letter.isupper():
            new_alphabet.append(letter.lower())
        else:
            new_alphabet.append(letter)
    encrypted = ''
    for c in s:
        index = c. ord() - 65
        if index >= 0 and index < len(new_alphabet):
            encrypted += new_alphabet[index]
        else:
            encrypted += c
    return encrypted