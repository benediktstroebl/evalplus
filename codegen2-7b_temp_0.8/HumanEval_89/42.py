
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
    alphabet = [chr(i) for i in range(97, 123)]
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i][::2] + alphabet[i][1:]
    return "".join(alphabet[i] for i in s)
