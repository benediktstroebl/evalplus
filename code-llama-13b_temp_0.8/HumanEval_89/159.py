
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
    cypher_dict = {'a': 'ab', 'b': 'cd', 'c': 'ef', 'd': 'gh', 'e': 'ij', 'f': 'kl', 'g': 'mn', 'h': 'op', 'i': 'qr', 'j': 'st', 'k': 'uv', 'l': 'wx', 'm': 'yz', 'n': 'ba', 'o': 'cd', 'p': 'ef', 'q': 'gh', 'r': 'ij', 's': 'kj', 't': 'lm', 'u': 'on', 'v': 'pq', 'w': 'rs', 'x': 'tu', 'y': 'vw', 'z': 'xz'}
    return ''.join(map(lambda x: cypher_dict.get(x, x), s))
