
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
    def shift(char):
        if char.isupper():
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return alphabet[(alphabet.index(char) + 4) % 26]
        elif char.islower():
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            return alphabet[(alphabet.index(char) + 4) % 26]
    result = ""
    for char in s:
        result += shift(char)
    return result

