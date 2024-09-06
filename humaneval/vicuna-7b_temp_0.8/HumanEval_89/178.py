
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
    shifted_alphabet = list(alphabet)
    for i in range(len(s)):
        shifted_alphabet[i], shifted_alphabet[i+1] = shifted_alphabet[i+1], shifted_alphabet[i]
    encrypted_string = ''.join(shifted_alphabet)
    return encrypted_string
