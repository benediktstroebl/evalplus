
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
    i = 0
    ans = ''
    while i < len(s):
        if ord(s[i]) + 2*2 < ord('z'):
            ans += chr(ord(s[i]) + 2*2)
        else:
            ans += chr(ord(s[i]) + 2*2 - 26)
        i+= 1
    return ans
