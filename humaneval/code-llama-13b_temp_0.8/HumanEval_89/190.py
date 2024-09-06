
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
    #myStr = 'abcdefghijklmnopqrstuvwxyz'
    newStr = ''
    for i in s:
        #print i
        if i in 'abc':
            newStr += 'e'
        elif i in 'def':
            newStr += 'g'
        elif i in 'ghi':
            newStr += 'j'
        elif i in 'jkl':
            newStr += 'm'
        elif i in 'mno':
            newStr += 'q'
        elif i in 'pqr':
            newStr += 't'
        elif i in 'stu':
            newStr += 'v'
        elif i in 'vwx':
            newStr += 'z'
        elif i in 'wxy':
            newStr += 'a'
        elif i in 'z':
            newStr += 'c'
        else:
            newStr += i
    return newStr
