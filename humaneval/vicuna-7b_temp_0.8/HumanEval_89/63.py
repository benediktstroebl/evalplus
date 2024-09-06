
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
    rotated_alphabet = list(alphabet)
    rotated_alphabet[::2] = rotated_alphabet[1::2][::-1]
    encrypted_string = ''
    for c in s:
        if c in rotated_alphabet:
            encrypted_string += rotated_alphabet.index(c)
        else:
            encrypted_string += c
    return encrypted_string
