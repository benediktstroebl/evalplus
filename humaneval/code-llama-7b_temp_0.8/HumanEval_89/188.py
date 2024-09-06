
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
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in s:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) + 2*2) % 26]
        else:
            result += c
    return result
