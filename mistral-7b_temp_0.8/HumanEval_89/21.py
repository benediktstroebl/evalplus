
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
    enc_str = ""
    for i in range(len(s)):
        s_i = ord(s[i])
        # s_i = s_i - ord('a')
        s_i += 2 * 2
        # s_i = s_i % 26
        # s_i += ord('a')
        enc_str += chr(s_i)
    return enc_str

