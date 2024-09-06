
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
    # TODO: Your code here
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = ''

    for i in range(len(alphabet)):
        if i % 2 == 0:
            continue
        key += alphabet[i]
        key += alphabet[i]
    return key
