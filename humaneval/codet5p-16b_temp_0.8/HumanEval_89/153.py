
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

    def alphabet(s):
        """Create a function alphabet that takes a string as an argument and
        returns a string with the alphabet being rotated. 
        The alphabet should be rotated in a manner such that the letters 
        shift down by two multiplied to two places.
        For example:
        alphabet('hi') returns 'lm'
        alphabet('asdfghjkl') returns 'ewhjklnop'
        alphabet('gf') returns 'kj'
        alphabet('et') returns 'ix'
        """
        return s[2:] + s[:2]

    return ''.join(alphabet(s)[i] for i in range(len(s)))
