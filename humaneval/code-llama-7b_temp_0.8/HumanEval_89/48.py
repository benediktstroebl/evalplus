
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
    s = s.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = abc[2:]+abc[:2]
    out = ''
    for i in s:
        if i in abc:
            out += abc[abc.find(i):abc.find(i)+1]
        else:
            out += i
    return out




    
