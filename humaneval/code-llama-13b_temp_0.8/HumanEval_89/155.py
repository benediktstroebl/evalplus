
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
    # Your code here

    dict_alphabet = {
        'a':'x',
        'b':'y',
        'c':'z',
        'd':'a',
        'e':'b',
        'f':'c',
        'g':'d',
        'h':'e',
        'i':'f',
        'j':'g',
        'k':'h',
        'l':'i',
        'm':'j',
        'n':'k',
        'o':'l',
        'p':'m',
        'q':'n',
        'r':'o',
        's':'p',
        't':'q',
        'u':'r',
        'v':'s',
        'w':'t',
        'x':'u',
        'y':'v',
        'z':'w',
    }

    result = []
    for word in s:
        result.append(dict_alphabet.get(word,word))
    return ''.join(result)
