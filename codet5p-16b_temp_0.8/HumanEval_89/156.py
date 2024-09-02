
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = ''
    for i in s:
        index = alphabet.index(i)
        new_index = index + 2 * 2
        if new_index > 25:
            new_index = new_index - 26
        encrypt = encrypt + alphabet[new_index]
    return encrypt
