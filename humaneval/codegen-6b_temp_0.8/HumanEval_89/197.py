
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
    new_string = ""
    for i in s:
        j = ord(i)
        if j >= 97 and j <= 122:
            j = j + 2
            j = j % 123
            new_string = new_string + chr(j)
        elif j >= 65 and j <= 90:
            j = j + 2
            j = j % 123
            new_string = new_string + chr(j)
        else:
            new_string = new_string + i
    return new_string
