
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
    for char in s:
        if not char.isalpha():
            continue
        if char.isupper():
            s = s.replace(char,''.join(sorted(char, key=lambda l: (ord(l)+2)//2, reverse=True)))
        else:
            s = s.replace(char,''.join(sorted(char, key=lambda l: (ord(l)+2)//2, reverse=True)))
    return s
