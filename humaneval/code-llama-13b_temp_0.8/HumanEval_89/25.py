
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
    
    result = ""
    
    for c in s:
        n = ord(c)
        
        if n >= 65 and n <= 90:
            if n > 90:
                n = n - 64 + 2
                n = n % 26 + 64
            else:
                n = n + 2
                if n > 90:
                    n = n - 64 + 2
                    n = n % 26 + 64
            result += chr(n)
        else:
            result += c
    
    return result
