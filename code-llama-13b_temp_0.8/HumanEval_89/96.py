
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
    import string
    if s == '':
        return ''
    new_str = ''
    for i in s:
        if i.isupper():
            new_str += chr(((ord(i)-ord('A')+2)%26) + ord('A'))
        elif i.islower():
            new_str += chr(((ord(i)-ord('a')+2)%26) + ord('a'))
        else:
            new_str += i
    return new_str
