
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
    string = 'abcdefghijklmnopqrstuvwxyz'
    z = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = ""
    for i in s:
        if i in string:
            if i == string[0]:
                encrypt = string[1]
            elif i == string[1]:
                encrypt = string[2]
            elif i == string[2]:
                encrypt = string[3]
            elif i == string[3]:
                encrypt = string[4]
            elif i == string[4]:
                encrypt = string[5]
            elif i == string[5]:
                encrypt = string[6]
            elif i == string[6]:
                encrypt = string[7]
            elif i == string[7]:
                encrypt = string[8]
            elif i == string[8]:
                encrypt = string[9]
            elif i == string[9]:
                encrypt = string[10]
            elif i == string
