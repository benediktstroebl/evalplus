
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s = ''.join(c for c in s if c in alphabet)
    cipher = ''
    for i in range(0, len(s)-1, 2):
        cipher += alphabet[alphabet.index(s[i]) + 2] + alphabet[alphabet.index(s[i+1]) + 2]
    if len(s) % 2 != 0:
        cipher += alphabet[alphabet.index(s[len(s)-1]) + 2]
    return cipher
