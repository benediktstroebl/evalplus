
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
    letter_list = [ch for ch in 'abcdefghijklmnopqrstuvwxyz']
    letter_list = [chr(ord(ch) + 2) for ch in letter_list]
    return ''.join(letter_list)
