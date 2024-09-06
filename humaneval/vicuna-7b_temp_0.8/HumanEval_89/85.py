
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
    s = s.upper()
    encrypted = []
    for char in s:
        if char.isalpha():
            index = ord(char) - 97
            if index >= 0 and index < 26:
                encrypted.append(chr(index + 26))
            elif index >= 26 and index < 52:
                encrypted.append(chr((index - 26) + 25))
            else:
                encrypted.append(chr(index))
        else:
            encrypted.append(char)
    return ''.join(encrypted)