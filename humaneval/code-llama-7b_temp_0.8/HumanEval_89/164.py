
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

    # transpose the string
    transposed = s[0::2] + s[1::2]

    # initialize new string
    encrypted = ''

    # loop through transposed string
    for i in transposed:
        # determine if lower or uppercase
        if i.islower():
            # add corresponding number
            encrypted += chr(int(ord(i) + 2*2)%26 + 97)
        else:
            # add corresponding number
            encrypted += chr(int(ord(i) + 2*2)%26 + 65)

    # return new string
    return encrypted
