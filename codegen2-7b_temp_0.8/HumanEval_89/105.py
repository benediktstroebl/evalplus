
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
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    key=lower+upper+lower+upper
    result=''
    for i in s:
        x=key.index(i)
        if x<5:
            x=x+2
        elif x<10:
            x=x+1
        result+=key[x]
    return result
