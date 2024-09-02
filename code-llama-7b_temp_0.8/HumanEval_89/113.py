
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
    c = 'abcdefghijklmnopqrstuvwxyz'
    e = c[2:] + c[:2]
    s = s.lower()
    new_string = ''
    for i in s:
        if i not in c:
            new_string += i
        else:
            new_string += e[c.index(i)]
    return new_string
