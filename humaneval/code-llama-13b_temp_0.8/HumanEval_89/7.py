
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
    # return s.lower().replace('a', 'o').replace('b', 'p').replace('c', 'q').replace('d', 'r').replace('e', 's').replace('f', 't').replace('g', 'u').replace('h', 'v').replace('i', 'w').replace('j', 'x').replace('k', 'y').replace('l', 'z').replace('m', 'a').replace('n', 'b').replace('o', 'c').replace('p', 'd').replace('q', 'e').replace('r', 'f').replace('s', 'g').replace('t', 'h').replace('u', 'i').replace('v', 'j').replace('w', 'k').replace('x', 'l').replace('y', 'm').replace('z', 'n')
    
    # return ''.join([chr((ord(i) - 2) % 26 + ord('a')) for i in s.lower()])
    
    return ''.join([chr((ord(i) + 2) % 26 + ord('a')) for i in s.lower()])
