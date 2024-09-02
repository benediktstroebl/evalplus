
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_shifted = letters[2:] + letters[:2]
    s = s.lower()
    result = ''
    for char in s:
        if char in letters:
            result += letters_shifted[letters.index(char)]
        else:
            result += char
    return result
