
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
    final = []
    for i in s:
        if i == 'a':
            final.append('j')
        elif i == 'b':
            final.append('k')
        elif i == 'c':
            final.append('l')
        elif i == 'd':
            final.append('m')
        elif i == 'e':
            final.append('n')
        elif i == 'f':
            final.append('o')
        elif i == 'g':
            final.append('p')
        elif i == 'h':
            final.append('q')
        elif i == 'i':
            final.append('r')
        elif i == 'j':
            final.append('s')
        elif i == 'k':
            final.append('t')
        elif i == 'l':
            final.append('u')
        elif i == 'm':
            final.append('v')
        elif i == 'n':
            final.append('w')
        elif i == 'o':
            final.append('x')
        elif i == 'p':
            final.append('y')
        elif i == 'q':
            final.append('z')
        elif i == 'r':
            final.append('a')
        elif i == 's':
            final.append('b')
        elif i == 't':
            final.append('c')
        elif i == 'u':
            final.append('d')
        elif i == 'v':
            final.append('e')
        elif i == 'w':
            final.append('f')
        elif i == 'x':
            final.append('g')
        elif i == 'y':
            final.append('h')
        elif i == 'z':
            final.append('i')
        else:
            final.append(i)
    
    return ''.join(final)
