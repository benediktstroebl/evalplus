
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
    s_len = len(s)
    s = s.lower()
    if s_len % 2 == 0:
        return s
    
    else:
        rot_index = int(s_len/2)
        cipher_text = ''
        for char in s:
            cipher_text += s[rot_index] + s[rot_index-1]
            rot_index -= 1
        
        return cipher_
