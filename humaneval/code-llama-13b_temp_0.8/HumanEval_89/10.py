
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
    for i, c in enumerate(s):
        char = ord(c)
        # checks if the char is a letter
        if(char >= 65 and char <= 90):
            s[i] = chr(((char - 65 + 2) % 26) + 65)
        if(char >= 97 and char <= 122):
            s[i] = chr(((char - 97 + 2) % 26) + 97)

    return ''.join(s)
