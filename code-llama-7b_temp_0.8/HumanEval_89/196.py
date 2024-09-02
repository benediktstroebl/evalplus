
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
    newstring = []
    for c in s:
        if (c >= 'a' and c <= 'z'):
            newstring.append(chr((ord(c) - ord('a') + 2 * 2) % 26 + ord('a')))
        elif (c >= 'A' and c <= 'Z'):
            newstring.append(chr((ord(c) - ord('A') + 2 * 2) % 26 + ord('A')))
        else:
            newstring.append(c)
    return "".join(newstring)
