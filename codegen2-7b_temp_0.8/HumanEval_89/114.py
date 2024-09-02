
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
    rot_alpha = [('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'),('m','n','o'),('p','q','r','s'),('t','u','v','w'),('x','y','z')]
    s = s.lower()
    return ''.join(rot_alpha[(alphabet.index(s[i])-alphabet.index(s[i-1]))%26][i%26] for i in range(len(s)))
