
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
    
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    newAlphabet = Alphabet[2:] + Alphabet[:2]
    newAlphabet = newAlphabet[1:] + newAlphabet[:1]
    
    return newAlphabet[Alphabet.find(s[0])] + encrypt(s[1:])
