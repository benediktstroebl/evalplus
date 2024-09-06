
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

    result = ""
    for i in s:
        if i.isalpha():
            if ord(i) - 2 <= ord('z') and ord(i) - 2 >= ord('a'):
                result += chr(ord(i) - 2)
            elif ord(i) - 2 > ord('z'):
                result += chr(ord(i) - 2 - 26)
            else:
                result += chr(ord(i) - 2 + 26)
        else:
            result += i
    return result
