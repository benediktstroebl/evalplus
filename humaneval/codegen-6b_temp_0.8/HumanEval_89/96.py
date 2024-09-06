
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
    rotated_alphabet = alphabet[-1:] + alphabet[:-1]
    table_list = [rotated_alphabet[rotated_alphabet.index(char)+2] + rotated_alphabet[(rotated_alphabet.index(char)+2) % len(rotated_alphabet)] for char in alphabet]
    table = ''.join(table_list)
    output = ''.join(table[table.index(char)+1] for char in s)
    return output
