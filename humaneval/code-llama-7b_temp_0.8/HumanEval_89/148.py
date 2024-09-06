
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
    s = list(s)
    newstr = []
    for i in s:
        if i.isupper():
            newstr.append(chr((ord(i) + 2*26) % 26 + ord('A')))
        elif i.islower():
            newstr.append(chr((ord(i) + 2*26) % 26 + ord('a')))
        else:
            newstr.append(i)
    return ''.join(newstr)

