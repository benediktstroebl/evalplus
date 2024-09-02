
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
    # Use a dictionary to map each letter to its new position in the alphabet
    map = {
        'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm',
        'f': 'n', 'g': 'o', 'h': 'p', 'i': 'q', 'j': 'r',
        'k': 's', 'l': 't', 'm': 'u', 'n': 'v', 'o': 'w',
        'p': 'x', 'q': 'y', 'r': 'z', 's': 'a', 't': 'b',
        'u': 'c', 'v': 'd', 'w': 'e', 'x': 'f', 'y': 'g',
        'z': 'h', 'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l',
        'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
        'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
        'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
        'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
        'z': 'a', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
        'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
        'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
        'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
        'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
        'z': 'a', 'b':
