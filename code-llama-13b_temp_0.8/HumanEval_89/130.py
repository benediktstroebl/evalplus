
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
    ascii_offset = 97
    
    def get_lower_ascii(c):
        return ord(c) - ascii_offset
    
    def get_lower_ascii_bound(a, b):
        return (a + b) % 26
    
    def get_letter(a):
        return chr(a + ascii_offset)
        
    def get_encrypted_letter(c):
        ascii_value = ord(c)
        if (ascii_value < 97 or ascii_value > 122):
            return c
        ascii_value = get_lower_ascii(c)
        ascii_value = get_lower_ascii_bound(ascii_value, 2)
        return get_letter(ascii_value)
    
    return ''.join([get_encrypted_letter(c) for c in s])
