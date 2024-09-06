
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
    s = s.lower()
    dict = {
        'a': 'fd', 'b': 'gc', 'c': 'hu', 'd': 'jv', 'e': 'lb', 'f': 'nm',
        'g': 'qz', 'h': 'ti', 'i': 'wxs', 'j': 'az', 'k': 'bce', 'l': 'df',
        'm': 'ghi', 'n': 'jkl', 'o': 'tp', 'p': 'uv', 'q': 'wxy', 'r': 'zac',
        's': 'bd', 't': 'eg', 'u': 'fh', 'v': 'gi', 'w': 'jkn', 'x': 'lo',
        'y': 'pm', 'z': 'qrs', ' ': ' '
    }
    output = ""
    for x in s:
        output += dict.get(x)
    return output

