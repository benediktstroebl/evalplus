
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

    # initialize a dictionary to map characters to their indices in the alphabet
    alphabet = {char:idx for idx, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    
    # initialize a dictionary to map indices to the new corresponding characters
    new_alphabet = {idx:(idx * 2) % 26 for idx in range(26)}
    
    # return a string of new characters corresponding to the old characters
    return ''.join(new_alphabet[alphabet[char]] for char in s.lower())

