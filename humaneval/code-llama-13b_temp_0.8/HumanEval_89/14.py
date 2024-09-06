
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
        if ord(letter) >= 65 and ord(letter) <= 90:
            if ord(letter) + 10 > 90:
                result += chr((ord(letter) + 10) - 26)
            else:
                result += chr(ord(letter) + 10)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            if ord(letter) + 10 > 122:
                result += chr((ord(letter) + 10) - 26)
            else:
                result += chr(ord(letter) + 10)
        else:
            result += letter
    return result
