
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
    # s = 'hi'
    # s = 'asdfghjkl'
    # s = 'gf'
    # s = 'et'
    encrypt = ''
    for x in s:
        if x == ' ':
            encrypt += ' '
        elif x.islower():
            encrypt += chr(97 + (ord(x) - 97 + 4) % 26)
        elif x.isupper():
            encrypt += chr(65 + (ord(x) - 65 + 4) % 26)
    return encrypt
