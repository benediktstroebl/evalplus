
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for i in range(len(s)):
        c = s[i]
        c = c.lower()
        if c not in alphabet:
            result += c
        else:
            rot = alphabet.find(c) + 2*2
            if rot > 26:
                rot -= 26
            result += alphabet[rot]
    return result
