
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
    # create a list to store the encrypted characters
    encrypted = [None] * 26
    # loop through each character in the input string
    for i, c in enumerate(s):
        # if the current character is not in the alphabet, replace it
        if c not in 'abcdefghijklmnopqrstuvwxyz':
            s[i] = '?'
            continue
        # add the current character to the encrypted list
        encrypted[s.index(c) // 2] = c
    return ''.join(encrypted)
