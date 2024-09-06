
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
    s = list(s)
    for i, letter in enumerate(s):
        if letter.isalpha():
            if letter.isupper():
                s[i] = chr(96 + (ord(letter) - 65 + 2) % 26)
            else:
                s[i] = chr(123 - (ord(letter) - 97 + 2) % 26)
    return ''.join(s)

