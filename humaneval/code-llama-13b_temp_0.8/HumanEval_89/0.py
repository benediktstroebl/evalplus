
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
    result = ''
    for letter in s:
        ascii_val = ord(letter)
        if ascii_val >= 65 and ascii_val <= 90:
            result += chr(ascii_val + 32 * 2)
        elif ascii_val >= 97 and ascii_val <= 122:
            result += chr(ascii_val + 32 * 2)
        else:
            result += letter
    return result

