
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
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    letter_map = {alphabet[i]: alphabet[(i+2)%26] for i in range(26)}
    #letter_map = {a:b for a,b in zip(alphabet,alphabet[1:])}
    
    #return ''.join(letter_map[x] for x in s)
    return ''.join(letter_map[x] for x in s.upper())
    # return ''.join(s[(i+2)%26] for i,x in enumerate(s))
