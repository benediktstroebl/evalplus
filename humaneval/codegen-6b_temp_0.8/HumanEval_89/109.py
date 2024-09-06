
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
    # Create a dictionary with the alphabet and the corresponding
    # shifted alphabet.
    rotated = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}

    # Turn the string argument into upper case characters
    s = s.upper()

    # Turn the characters of the string argument into elements of a list
    newlist = list(s)

    # Create a new list that will store the encrypted string
    newlist2 = []

    # Loop through the list
    for i in newlist:
        # TODO: Add a conditional that checks if the element of the list is a
        # character in the rotated dictionary and add the encrypted character
        # to the new list
        newlist2.append(rotated.get(i, None))

    # Turn the new list into a string
    ans = ''.join(newlist2)
    return ans
