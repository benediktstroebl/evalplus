
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
    result = ''
    shift = 2
    for char in s:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % len(alphabet)
            result += alphabet[new_idx]
        else:
            result += char
    return result
