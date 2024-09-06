
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
    #I don't know how to make this faster.
    #Alphabet dicts are in the form:
    #{'a':'s', 'b':'t', 'c':'u', ...}
    #Alphabet dicts are in the form:
    #{'a':'s', 'b':'t', 'c':'u', ...}
    alphabet = {'a':'s', 'b':'t', 'c':'u', 'd':'v', 'e':'w', 'f':'x', 
    'g':'y', 'h':'z', 'i':'a', 'j':'b', 'k':'c', 'l':'d', 'm':'e', 'n':'f', 'o':'g', 
    'p':'h', 'q':'i', 'r':'j', 's':'k', 't':'l', 'u':'m', 'v':'n', 'w':'o', 'x':'p',
    'y':'q', 'z':'r'}
    #Sets encrypts the string and drops the middle two letters.
    #eg encrypt('hi') returns 'lm'
    s2 = s[:2] + s[len(s) - 2:]
    #then sets the second and last letters equal to each other
    #eg encrypt('asdfghjkl') returns 'ewhjklnop'
    s3 = s2[0] + s2[len(s2) - 1]
    #then I will decompose the string into a list with each letter in it.
    #eg. ['h', 'i', 's', 'd', 'f', 'g', 'k', 'l', 'a', 'm', 'e', 'w', 'h', 'j', 'k', 'l', 'n', 'o', 'p', 'o', 'p']
    l = list(s3)
    #then I will create a new list with each letter replaced with the alphabet
    #replaced with the number and letter in the alphabet subtracted by two times 32.
    #eg. ['s', 't', 'u', 'v', '