
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
    for i in range(0, len(alphabet), 2):
        temp = alphabet[i]
        alphabet[i] = alphabet[i + 1]
        alphabet[i + 1] = temp
    return "".join([alphabet[alphabet.index(letter) + 2] for letter in s])
