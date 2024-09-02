
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
    def rot_2(s):
        s1 = ""
        for c in s:
            if c.isupper():
                x = ord(c)+2
                if x > ord('Z'):
                    x -= 26
                s1 += chr(x)
            elif c.islower():
                x = ord(c)+2
                if x > ord('z'):
                    x -= 26
                s1 += chr(x)
            else:
                s1 += c
        return s1
    return rot_2(rot_2(s))
