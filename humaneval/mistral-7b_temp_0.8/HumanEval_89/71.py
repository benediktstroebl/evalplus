
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
    # change the string into a list of characters
    char_list = list(s)
    # list comprehension - create a new list with new characters
    encrypted_char_list = [chr((ord(x) - ord('a') + 2) % 26 + ord('a')) for x in char_list]
    # join the new list of characters into a string and return it
    return ''.join(encrypted_char_list)
