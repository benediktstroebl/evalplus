
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
    cipher_text = ""
    for c in s:
        i = alphabet.index(c)
        i_ = i + 2*2
        if i_ > len(alphabet)-1:
            i_ = i_ - len(alphabet)
        cipher_text = cipher_text + alphabet[i_]
    return cipher_text

