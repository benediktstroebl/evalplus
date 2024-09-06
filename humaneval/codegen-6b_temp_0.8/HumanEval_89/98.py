
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
    code_dict = {'a':'w','b':'x','c':'y','d':'z','e':'a','f':'b','g':'c','h':'d','i':'e','j':'f','k':'g','l':'h','m':'i','n':'j','o':'k','p':'l','q':'m','r':'n','s':'o','t':'p','u':'q','v':'r','w':'s','x':'t','y':'u','z':'v'}
    answer = ""
    for letter in s:
        answer += code_dict[letter]
    return answer
