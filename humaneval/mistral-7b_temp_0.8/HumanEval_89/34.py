
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
    encrypt_string = ""
    for i in s:
        index = ord(i)
        if index >= 65 and index <= 90:
            encrypt_string += chr(65+(index-65-2)*2)
        elif index >= 97 and index <= 122:
            encrypt_string += chr(97+(index-97-2)*2)
        elif index == 32:
            encrypt_string += " "
    return encrypt_string


