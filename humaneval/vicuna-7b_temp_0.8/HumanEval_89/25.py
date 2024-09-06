
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
    string = s.lower()
    new_string = ''
    for char in string:
        if char.isalpha():
            new_char = chr((ord(char) - 97) // 2) + chr((ord(char) - 97) % 2)
            new_string += new_char
        else:
            new_string += chr(ord(char) // 2)
    return new_string.upper()
