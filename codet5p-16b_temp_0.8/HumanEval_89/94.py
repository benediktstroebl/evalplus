
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

    encryption = ""
    for i in range(len(s)):
        newLetter = ord(s[i]) + 2
        if newLetter > 122:
            newLetter = 97 + (newLetter - 122) - 1
            encryption += chr(newLetter)
        else:
            encryption += chr(newLetter)
    return encryption
