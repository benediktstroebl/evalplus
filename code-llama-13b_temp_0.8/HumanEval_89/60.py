
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
    # start out with an empty string
    encrypted = ''
    for c in s:
        # for each char, convert to a number
        # add 2 to it and then convert back
        # to a char and add that to the string
        # (encrypt the char)
        encrypted = encrypted + chr((ord(c) - 96 + 2) % 26 + 96)
    return encrypted
