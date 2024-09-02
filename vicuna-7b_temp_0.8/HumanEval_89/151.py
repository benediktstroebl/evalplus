
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
    key = []
    for i in range(27):
        key.append(chr(ord('a') + i))
    result = ""
    for c in s:
        result += key.pop(0)
    while len(key) > 0:
        result += chr(ord('a') + key[0])
        key.pop(0)
    return result
