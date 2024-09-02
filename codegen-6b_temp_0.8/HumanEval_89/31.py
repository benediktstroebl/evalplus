
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
    
    alpha_dict = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u',
                  'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o',
                  'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i',
                  's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c',
                  'y':'b', 'z':'a'}
    encrypted = ''
    s = s.lower()
    for i in s:
        if i in alpha_dict:
            encrypted += alpha_dict[i]
    return encrypted

