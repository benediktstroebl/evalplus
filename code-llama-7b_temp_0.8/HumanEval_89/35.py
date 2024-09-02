
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
    char = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in s:
        if i in char:
            result += char[(char.index(i) + 4) % len(char)]
        else:
            result += i
    return result
