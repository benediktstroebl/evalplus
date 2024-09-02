
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
    
    caesar = {}
    
    for index, letter in enumerate(alphabet):
        caesar[letter] = index

    count = 0
    for index, letter in enumerate(alphabet):
        count += index
        caesar[letter] = count
    
    return ''.join([caesar[letter] for letter in s])
    
