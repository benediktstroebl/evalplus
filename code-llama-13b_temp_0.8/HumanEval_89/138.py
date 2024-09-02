
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
    ls = list(s)
    for i, v in enumerate(s):
        if v == 'a':
            ls[i] = 'd'
        elif v == 'b':
            ls[i] = 'e'
        elif v == 'c':
            ls[i] = 'f'
        elif v == 'd':
            ls[i] = 'g'
        elif v == 'e':
            ls[i] = 'h'
        elif v == 'f':
            ls[i] = 'i'
        elif v == 'g':
            ls[i] = 'j'
        elif v == 'h':
            ls[i] = 'k'
        elif v == 'i':
            ls[i] = 'l'
        elif v == 'j':
            ls[i] = 'm'
        elif v == 'k':
            ls[i] = 'n'
        elif v == 'l':
            ls[i] = 'o'
        elif v == 'm':
            ls[i] = 'p'
        elif v == 'n':
            ls[i] = 'q'
        elif v == 'o':
            ls[i] = 'r'
        elif v == 'p':
            ls[i] = 's'
        elif v == 'q':
            ls[i] = 't'
        elif v == 'r':
            ls[i] = 'u'
        elif v == 's':
            ls[i] = 'v'
        elif v == 't':
            ls[i] = 'w'
        elif v == 'u':
            ls[i] = 'x'
        elif v == 'v':
            ls[i] = 'y'
        elif v == 'w':
            ls[i] = 'z'
        elif v == 'x':
            ls[i] = 'a'
        elif v == 'y':
            ls[i] = 'b'
        elif v == 'z':
            ls[i] = 'c'
        elif v == 'A':
            ls[i] = 'D'
        elif v == 'B':
