
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
    string = list(s)
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            if ord(string[i]) >= 114 and ord(string[i]) <= 122:
                string[i] = chr(107+ord(string[i]))
            elif ord(string[i]) <= 113:
                string[i] = chr(ord(string[i])+2)
        elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
            if ord(string[i]) >= 79 and ord(string[i]) <= 90:
                string[i] = chr(87+ord(string[i]))
            elif ord(string[i]) <= 78:
                string[i] = chr(ord(string[i])+2)
    return "".join(string)
