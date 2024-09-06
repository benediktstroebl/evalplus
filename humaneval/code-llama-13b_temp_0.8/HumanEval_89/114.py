
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
    import string
    s = s.lower()
    letters = list(string.ascii_lowercase)
    letters2 = letters[2:] + letters[:2]
    new_letters = dict(zip(letters, letters2))
    return ''.join(new_letters.get(i, i) for i in s)

