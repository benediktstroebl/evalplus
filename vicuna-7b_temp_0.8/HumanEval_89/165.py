
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
    # Create a dictionary of the rotated alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[::-1] + alphabet[:1]
    # Use a list comprehension to create a new string
    # containing the encrypted value of the input string
    return ''.join([rotated_alphabet[i] if i % 2 == 0 else i for i in s])
