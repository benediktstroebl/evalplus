
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
    #Your code here
    rot=len(s)*2
    en=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                en+=chr(((ord(i)-ord('A')+rot)%26)+ord('A'))
            else:
                en+=chr(((ord(i)-ord('a')+rot)%26)+ord('a'))
        else:
            en+=i
    return en

