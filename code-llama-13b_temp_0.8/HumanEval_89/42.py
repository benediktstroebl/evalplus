
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
    # Your code here
    s = list(s)
    for idx, ltr in enumerate(s):
        letter_ord = ord(s[idx])
        if 97 <= letter_ord <= 122:
            s[idx] = chr(122 - (letter_ord - 97) * 2)
        else:
            s[idx] = chr(90 - (letter_ord - 65) * 2)
    return "".join(s)

