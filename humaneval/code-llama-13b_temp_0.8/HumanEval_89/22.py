
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
    new_alphabet = ''
    for i in range(1, 26, 2):
        new_alphabet += alphabet[i:i+2]
        new_alphabet += alphabet[:i]
    new_s = ''
    for letter in s:
        index = alphabet.find(letter)
        new_s += new_alphabet[index]
    return new_s
