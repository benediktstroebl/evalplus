
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
    
    # The character to shift down by, add to in-place
    char_shift = ord('a')
    # The character to shift right by, add to in-place
    char_shift_add = 2
    # The string to encrypt
    string = s
    # The string to return
    result = ''
    # Iterate over string
    for ch in string:
        # Add shifted character to result
        result += chr((ord(ch) - char_shift) + char_shift_add)
    
    return result

