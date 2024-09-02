
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
    s = s.lower()
    result = ''
    for x in s:
        if x == 'a':
            result += 'b'
        elif x == 'b':
            result += 'c'
        elif x == 'c':
            result += 'd'
        elif x == 'd':
            result += 'e'
        elif x == 'e':
            result += 'f'
        elif x == 'f':
            result += 'g'
        elif x == 'g':
            result += 'h'
        elif x == 'h':
            result += 'i'
        elif x == 'i':
            result += 'j'
        elif x == 'j':
            result += 'k'
        elif x == 'k':
            result += 'l'
        elif x == 'l':
            result += 'm'
        elif x == 'm':
            result += 'n'
        elif x == 'n':
            result += 'o'
        elif x == 'o':
            result += 'p'
        elif x == 'p':
            result += 'q'
        elif x == 'q':
            result += 'r'
        elif x == 'r':
            result += 's'
        elif x == 's':
            result += 't'
        elif x == 't':
            result += 'u'
        elif x == 'u':
            result += 'v'
        elif x == 'v':
            result += 'w'
        elif x == 'w':
            result += 'x'
        elif x == 'x':
            result += 'y'
        elif x == 'y':
            result += 'z'
        elif x == 'z':
            result += 'a'
        else:
            result += x
    return result
