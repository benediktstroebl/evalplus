
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
    s2 = []
    for char in s:
        if char == 'a':
            s2.append('g')
        if char == 'b':
            s2.append('h')
        if char == 'c':
            s2.append('i')
        if char == 'd':
            s2.append('j')
        if char == 'e':
            s2.append('k')
        if char == 'f':
            s2.append('l')
        if char == 'g':
            s2.append('m')
        if char == 'h':
            s2.append('n')
        if char == 'i':
            s2.append('o')
        if char == 'j':
            s2.append('p')
        if char == 'k':
            s2.append('q')
        if char == 'l':
            s2.append('r')
        if char == 'm':
            s2.append('s')
        if char == 'n':
            s2.append('t')
        if char == 'o':
            s2.append('u')
        if char == 'p':
            s2.append('v')
        if char == 'q':
            s2.append('w')
        if char == 'r':
            s2.append('x')
        if char == 's':
            s2.append('y')
        if char == 't':
            s2.append('z')
        if char == 'u':
            s2.append('a')
        if char == 'v':
            s2.append('b')
        if char == 'w':
            s2.append('c')
        if char == 'x':
            s2.append('d')
        if char == 'y':
            s2.append('e')
        if char == 'z':
            s2.append('f')
        if char == 'A':
            s2.append('G')
        if char == 'B':
            s2.append('H')
        if char == 'C':
            s2.append('I
