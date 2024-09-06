
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
    cipher = {'a': 'fp', 'b': 'lw', 'c': 'wf', 'd': 'tq', 'e': 'tr',
              'f': 'yq', 'g': 'bw', 'h': 'jk', 'i': 'yb', 'j': 'kz',
              'k': 'ez', 'l': 'a', 'm': 'f', 'n': 'ol', 'o': 'q2',
              'p': 'vb', 'q': 'as', 'r': 'w', 's': 'd', 't': 't',
              'u': 'd', 'v': 't', 'w': 'r', 'x': 'r', 'y': 'x',
              'z': 'j', ' ': ' ', '.': '.'}

    return ''.join([cipher.get(i, i) for i in s if i not in ' .'])

