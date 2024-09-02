
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
    # use a dictionary to map the original alphabet to the rotated alphabet
    map = {
        'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 
        'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 
        'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 
        'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 
        'r': 's', 's': 't', 't': 'u', 'u': 'v', 
        'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 
        'z': 'a', 'a': 'b'
    }
    result = []
    for char in s:
        if char.isalpha():
            result.append(map[char.lower()[::-1]])
        else:
            result.append(char)
    return ''.join(result)
