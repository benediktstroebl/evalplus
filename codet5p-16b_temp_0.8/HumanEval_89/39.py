
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
    encrypted = ""
    for i in range(len(s)):
        if s[i] in alphabet:
            encrypted += alphabet[(alphabet.index(s[i]) + 2 * 2) % len(alphabet)]
        else:
            encrypted += s[i]
    return encrypted
