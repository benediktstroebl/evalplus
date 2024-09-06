
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
    chars = list(s)
    letters = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(chars)):
        if chars[i] in letters:
            pos = letters.index(chars[i]) + 2 ** 2
            if pos > 25:
                pos -= 26
            chars[i] = letters[pos]
    return ''.join(chars)

