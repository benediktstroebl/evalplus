
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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if alphabet[i] == s[0]:
            return alphabet[i + 2 * 2] + alphabet[i + 2 * 2 + 1] + alphabet[i + 2 * 2 + 2]
