
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
    enc = ""
    for i in range(len(s)):
        if s[i] == 'a':
            enc += 'e'
        elif s[i] == 'b':
            enc += 'h'
        elif s[i] == 'c':
            enc += 'k'
        elif s[i] == 'd':
            enc += 'm'
        elif s[i] == 'e':
            enc += 'a'
        elif s[i] == 'f':
            enc += 'b'
        elif s[i] == 'g':
            enc += 'c'
        elif s[i] == 'h':
            enc += 'd'
        elif s[i] == 'i':
            enc += 'f'
        elif s[i] == 'j':
            enc += 'g'
        elif s[i] == 'k':
            enc += 'l'
        elif s[i] == 'l':
            enc += 'h'
        elif s[i] == 'm':
            enc += 'n'
        elif s[i] == 'n':
            enc += 'i'
        elif s[i] == 'o':
            enc += 'j'
        elif s[i] == 'p':
            enc += 'o'
        elif s[i] == 'q':
            enc += 'q'
        elif s[i] == 'r':
            enc += 'r'
        elif s[i] == 's':
            enc += 's'
        elif s[i] == 't':
            enc += 't'
        elif s[i] == 'u':
            enc += 'u'
        elif s[i] == 'v':
            enc += 'v'
        elif s[i] == 'w':
            enc += 'w'
        elif s[i] == 'x':
            enc += 'x'
        elif s[i] == 'y':
            enc += 'y'
        elif s[i] == 'z':
            enc += 'z'
        else:
            enc += s[i]
    return enc
