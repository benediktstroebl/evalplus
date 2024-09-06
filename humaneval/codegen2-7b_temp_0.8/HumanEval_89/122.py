
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
    x = 2
    shift = 0
    r = ''
    for i in s:
        if i in alphabet:
            r += alphabet[(alphabet.index(i) - x) % len(alphabet)]
        else:
            r += i
            shift += 2
    if shift % 2:
        r = r[::-1]
    return
