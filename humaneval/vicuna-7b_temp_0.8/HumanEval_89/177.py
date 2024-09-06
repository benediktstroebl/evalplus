
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
    if len(s) < 2:
        return s
    if len(s) % 2 == 0:
        s = ''.join(chr(ord(c) // 2 + 97) for c in s)
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.upper()
        return s
    elif len(s) % 2 == 1:
        s = ''.join(chr(ord(c) // 2 + 97) for c in s[::-1])
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.upper()
        return s

s = "hello"
