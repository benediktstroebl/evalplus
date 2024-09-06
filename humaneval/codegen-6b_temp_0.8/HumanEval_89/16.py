
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
    encrypted_str = ""
    for c in s:
        if not c.isalpha():
            encrypted_str += c
            continue
        original_idx = ord(c) - ord("a")
        encrypted_idx = (original_idx + 2) % 26
        encrypted_str += chr(ord("a") + encrypted_idx)
    return encrypted_str

