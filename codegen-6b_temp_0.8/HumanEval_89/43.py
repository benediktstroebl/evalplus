
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
    
    def encrypt(s):
        """Encrypts a string with the alphabet being rotated by s characters"""
        alp = "abcdefghijklmnopqrstuvwxyz"
        cipher = ""
        for i in s:
            if i in alp:
                pos = alp.index(i)
                cipher += alp[(pos + s) % 26]
            else:
                cipher += i
        return cipher
    
    return encrypt
    