
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
    l = []
    for i in s:
        l.append(i)
    x = 2
    while len(l) > 0:
        l1 = []
        for i in range(len(l)):
            if l[i] == 'z':
                l1.append('a')
            elif l[i] == 'Z':
                l1.append('A')
            elif l[i] == 'y':
                l1.append('b')
            elif l[i] == 'Y':
                l1.append('B')
            elif l[i] == 'x':
                l1.append('c')
            elif l[i] == 'X':
                l1.append('C')
            elif l[i] == 'w':
                l1.append('d')
            elif l[i] == 'W':
                l1.append('D')
            elif l[i] == 'v':
                l1.append('e')
            elif l[i] == 'V':
                l1.append('E')
            elif l[i] == 'u':
                l1.append('f')
            elif l[i] == 'U':
                l1.append('F')
            elif l[i] == 't':
                l1.append('g')
            elif l[i] == 'T':
                l1.append('G')
            elif l[i] == 's':
                l1.append('h')
            elif l[i] == 'S':
                l1.append('H')
            elif l[i] == 'r':
                l1.append('i')
            elif l[i] == 'R':
                l1.append('I')
            elif l[i] == 'q':
                l1.append('j')
            elif l[i] == 'Q':
                l1.append('J')
            elif l[i] == 'p':
                l1.append('k')
            elif l[i] == 'P':
                l1.append('K')
            elif l[i] == 'o':
                l1.append('l
