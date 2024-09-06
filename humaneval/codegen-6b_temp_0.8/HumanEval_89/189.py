
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
    def encrypt(plaintext):
        #return plaintext.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'fghijklmnopqrstuvwxyzabc'))
        return ''.join(a+b for a,b in itertools.zip_longest(plaintext, alphabet[:26], fillvalue=''))
    return encrypt

