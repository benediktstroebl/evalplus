
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
    s_array = list(s)
    for i in range(len(s)):
        if s_array[i] == 'a':
            s_array[i] = 'q'
        elif s_array[i] == 'b':
            s_array[i] = 'r'
        elif s_array[i] == 'c':
            s_array[i] = 's'
        elif s_array[i] == 'd':
            s_array[i] = 't'
        elif s_array[i] == 'e':
            s_array[i] = 'u'
        elif s_array[i] == 'f':
            s_array[i] = 'v'
        elif s_array[i] == 'g':
            s_array[i] = 'w'
        elif s_array[i] == 'h':
            s_array[i] = 'x'
        elif s_array[i] == 'i':
            s_array[i] = 'y'
        elif s_array[i] == 'j':
            s_array[i] = 'z'
        elif s_array[i] == 'k':
            s_array[i] = 'a'
        elif s_array[i] == 'l':
            s_array[i] = 'b'
        elif s_array[i] == 'm':
            s_array[i] = 'c'
        elif s_array[i] == 'n':
            s_array[i] = 'd'
        elif s_array[i] == 'o':
            s_array[i] = 'e'
        elif s_array[i] == 'p':
            s_array[i] = 'f'
        elif s_array[i] == 'q':
            s_array[i] = 'g'
        elif s_array[i] == 'r':
            s_array[i] = 'h'
        elif s_array[i] == 's':
            s_array[i] = 'i'
        elif s_array[i] == 't':
            s_
