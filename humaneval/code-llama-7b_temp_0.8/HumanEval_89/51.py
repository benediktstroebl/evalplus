
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
    encrpyted_string = ""
    for letter in s:
        # to shift down by two multiplied by two places, just subtract 2 from 26.
        # By adding 26, we can get the desired shift in the string.
        encrpyted_string += chr((ord(letter) - 2) % 26 + 65)
    return encrpyted_string
