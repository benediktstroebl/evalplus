
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
    # Base case: empty string.
    if s == "":
        return s

    # Let's start by shifting each character by two multiples.
    s = s[0] + s[1:][0] + s[1:][1:][0] + s[1:][1:][1:]

    # Now the first two characters should be shifted down by two.
    s = s[2:] + s[:2]

    return s

