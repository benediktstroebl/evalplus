
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
    rotated = []
    letters = list(string.ascii_lowercase)
    for i in range(0, len(letters)):
        rotated.append(letters[i+2])
    rotated.append(letters[0])
    return ''.join(rotated[ord(l)-97] for l in s)
    #return ''.join((rotated[ord(l)-97] for l in s))
