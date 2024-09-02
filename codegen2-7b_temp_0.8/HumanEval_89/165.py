
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
    alphabet = string.ascii_lowercase
    if isinstance(s, str):
        for i in range(len(s)):
            if s[i] in alphabet:
                ind = alphabet.index(s[i])
                alphabet.insert(ind+2, alphabet.pop(ind))
        return ''.join(alphabet)
    else:
        print('type error')
    



