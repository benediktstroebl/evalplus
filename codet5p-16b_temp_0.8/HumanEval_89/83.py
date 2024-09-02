
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
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] ='m'
        if s[i] == 'b':
            s[i] = 'v'
        if s[i] == 'c':
            s[i] = 'z'
        if s[i] == 'd':
            s[i] = 'y'
        if s[i] == 'e':
            s[i] = 'q'
        if s[i] == 'f':
            s[i] = 'l'
        if s[i] == 'g':
            s[i] = 'w'
        if s[i] == 'h':
            s[i] = 'x'
        if s[i] == 'i':
            s[i] = 'a'
        if s[i] == 'j':
            s[i] ='s'
        if s[i] == 'k':
            s[i] = 'd'
        if s[i
