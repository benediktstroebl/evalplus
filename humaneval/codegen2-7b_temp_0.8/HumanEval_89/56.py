
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
    
    for char in alphabet:
        if char in s:
            return char + alphabet[alphabet.index(char) - 2] + s[len(alphabet) - 2:]
        else:
            return char + s[len(alphabet) - 1]
        
