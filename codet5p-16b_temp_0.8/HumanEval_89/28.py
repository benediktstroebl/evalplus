
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

    return ''.join(list(filter(lambda x: x not in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a','s', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n','m'], s)))[2:]+'m'+''.join(list(filter(lambda x: x not in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a','s', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n','m'], s)))[:2]

