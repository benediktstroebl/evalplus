
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
    letters = {
        'a':'y', 'b':'z', 'c':'a', 'd':'b', 'e':'c', 'f':'d', 'g':'e', 'h':'f', 'i':'g', 'j':'h', 'k':'i', 'l':'j', 'm':'k', 'n':'l', 'o':'m', 'p':'n', 'q':'o', 'r':'p', 's':'q', 't':'r', 'u':'s', 'v':'t', 'w':'u', 'x':'v', 'y':'w', 'z':'x'
    }
    result = ""
    for c in s:
        if c.isalpha():
            result += letters[c.lower()] if c.isupper() else letters[c]
        else:
            result += c
    return result
