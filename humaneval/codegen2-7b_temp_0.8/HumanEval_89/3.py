
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
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    s_len = len(s)
    def encrypt(s):
        ans = ""
        for i in range(s_len):
            ans += alphabet[(alphabet.index(s[i]) + s_len) % 26]
        return ans
    return
