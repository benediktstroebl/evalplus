
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
    s = list(s)
    for i, c in enumerate(s):
        if c == 'a':
            s[i] = 'j'
        elif c == 'b':
            s[i] = 'k'
        elif c == 'c':
            s[i] = 'l'
        elif c == 'd':
            s[i] = 'm'
        elif c == 'e':
            s[i] = 'n'
        elif c == 'f':
            s[i] = 'o'
        elif c == 'g':
            s[i] = 'p'
        elif c == 'h':
            s[i] = 'q'
        elif c == 'i':
            s[i] = 'r'
        elif c == 'j':
            s[i] = 's'
        elif c == 'k':
            s[i] = 't'
        elif c == 'l':
            s[i] = 'u'
        elif c == 'm':
            s[i] = 'v'
        elif c == 'n':
            s[i] = 'w'
        elif c == 'o':
            s[i] = 'x'
        elif c == 'p':
            s[i] = 'y'
        elif c == 'q':
            s[i] = 'z'
        elif c == 'r':
            s[i] = 'a'
        elif c == 's':
            s[i] = 'b'
        elif c == 't':
            s[i] = 'c'
        elif c == 'u':
            s[i] = 'd'
        elif c == 'v':
            s[i] = 'e'
        elif c == 'w':
            s[i] = 'f'
        elif c == 'x':
            s[i] = 'g'
        elif c == 'y':
            s[i] = 'h'
        elif c == 'z':
            s[i] = 'i'
    return ''.join(s)
