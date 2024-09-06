
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
    rotate = {'a':'e',
              'b':'f',
              'c':'g',
              'd':'h',
              'e':'i',
              'f':'j',
              'g':'k',
              'h':'l',
              'i':'m',
              'j':'n',
              'k':'o',
              'l':'p',
              'm':'q',
              'n':'r',
              'o':'s',
              'p':'t',
              'q':'u',
              'r':'v',
              's':'w',
              't':'x',
              'u':'y',
              'v':'z',
              'w':'a',
              'x':'b',
              'y':'c',
              'z':'d',
              ' ':' '}
    rotate_string = ""
    for letter in s:
        if letter in rotate:
            rotate_string += rotate[letter]
        else:
            rotate_string += letter
    return rotate_string
