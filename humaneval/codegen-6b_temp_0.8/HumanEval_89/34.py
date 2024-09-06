
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
    alphabet = list(string.ascii_lowercase)

    crypt_alphabet = alphabet[2:] + alphabet[:2]
    dct = {alphabet[i]: crypt_alphabet[i] for i in range(len(alphabet))}

    return ''.join(dct[char] for char in s)
