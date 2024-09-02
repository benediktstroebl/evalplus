
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
    return s.lower().replace('a', 'xx').replace('b', 'y').replace('c', 'z').replace('d', 'a') \
            .replace('e', 'b').replace('f', 'c').replace('g', 'd').replace('h', 'e') \
            .replace('i', 'f').replace('j', 'g').replace('k', 'h').replace('l', 'i') \
            .replace('m', 'j').replace('n', 'k').replace('o', 'l').replace('p', 'm') \
            .replace('q', 'n').replace('r', 'o').replace('s', 'p').replace('t', 'q') \
            .replace('u', 'r').replace('v', 's').replace('w', 't').replace('x', 'u') \
            .replace('y', 'v').replace('z', 'w').replace('xx', 'a').replace('y', 'b')
