
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
    newStr = ''
    alph = list('abcdefghijklmnopqrstuvwxyz')
    for i in s:
        index = alph.index(i)
        newIndex = index - 4
        if index < 4:
            newIndex = newIndex + 26
        newStr = newStr + alph[newIndex]
    return newStr
    
