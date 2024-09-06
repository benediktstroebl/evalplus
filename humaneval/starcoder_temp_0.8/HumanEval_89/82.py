
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
    d = {'a':'c','b':'d','c':'e','d':'f','e':'g','f':'h','g':'i','h':'j','i':'k','j':'l','k':'m','l':'n','m':'o','n':'p','o':'q','p':'r','q':'s','r':'t','s':'u','t':'v','u':'w','v':'x','w':'y','x':'z','y':'a','z':'b'}
    return ''.join([d[c] for c in s])

