
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
    string = s
    for i in range(len(string)):
        temp = string[i]
        if i < len(string) - 1:
            string[i] = string[i + 1]
            string[i + 1] = temp
        elif i == len(string) - 1:
            string = string[:i] + string[i + 2:]
    return string
