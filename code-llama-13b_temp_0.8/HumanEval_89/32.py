
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
        #a
        if s[i] == 'a':
            s[i] = 'k'
        #b
        elif s[i] == 'b':
            s[i] = 'l'
        #c
        elif s[i] == 'c':
            s[i] = 'm'
        #d
        elif s[i] == 'd':
            s[i] = 'n'
        #e
        elif s[i] == 'e':
            s[i] = 'o'
        #f
        elif s[i] == 'f':
            s[i] = 'p'
        #g
        elif s[i] == 'g':
            s[i] = 'q'
        #h
        elif s[i] == 'h':
            s[i] = 'r'
        #i
        elif s[i] == 'i':
            s[i] = 's'
        #j
        elif s[i] == 'j':
            s[i] = 't'
        #k
        elif s[i] == 'k':
            s[i] = 'u'
        #l
        elif s[i] == 'l':
            s[i] = 'v'
        #m
        elif s[i] == 'm':
            s[i] = 'w'
        #n
        elif s[i] == 'n':
            s[i] = 'x'
        #o
        elif s[i] == 'o':
            s[i] = 'y'
        #p
        elif s[i] == 'p':
            s[i] = 'z'
        #q
        elif s[i] == 'q':
            s[i] = 'a'
        #r
        elif s[i] == 'r':
            s[i] = 'b'
        #s
        elif s[i] == 's':
            s[i] = 'c'
        #t
        elif s[i] == 't':
            s[
