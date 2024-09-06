
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
    s = s.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_letters = letters[-2:] + letters[:-2]
    new_s = ''
    for i in s:
        if i in letters:
            new_index = letters.find(i) + 2
            new_s += new_letters[new_index]
        else:
            new_s += i
    return new_s

