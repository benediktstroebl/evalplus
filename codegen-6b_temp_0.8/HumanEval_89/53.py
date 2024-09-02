
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
    # Add your code here
    result = ""
    for i in s:
        char = ord(i)
        if char >= ord('a') and char <= ord('z'):
            char += 2
        elif char >= ord('A') and char <= ord('Z'):
            char += 2
        result += chr(char)
    return result
