
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
    string = {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u',
              'g': 'v', 'h': 'w', 'i': 'x', 'j': 'y', 'k': 'z', 'l': 'a',
              'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 'r': 'g',
              's': 'h', 't': 'i', 'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm',
              'y': 'n', 'z': 'o'}
    new_string = ''
    for letter in s:
        new_string += string[letter]
    return new_string

