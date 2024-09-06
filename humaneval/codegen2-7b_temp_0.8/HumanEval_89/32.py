
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
    return (s.replace('e', '3')
           .replace('t', '8')
           .replace('o', '1')
           .replace('i', '2')
           .replace('n', '6')
           .replace('s', '5')
           .replace('d', '4')
           .replace('f', '9')
           .replace('g', '7')
           .replace('h', '0')
           .replace('k', '8')
           .replace('j', '1')
           .replace('l', '2
