
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
    s = s.replace(' ', '')
    s_list = list(s)
    for index, letter in enumerate(s_list):
        if letter == 'z':
            s_list[index] = 'a'
        elif letter == 'y':
            s_list[index] = 'b'
        elif letter == 'x':
            s_list[index] = 'c'
        elif letter == 'w':
            s_list[index] = 'd'
        elif letter == 'v':
            s_list[index] = 'e'
        elif letter == 'u':
            s_list[index] = 'f'
        elif letter == 't':
            s_list[index] = 'g'
        elif letter == 's':
            s_list[index] = 'h'
        elif letter == 'r':
            s_list[index] = 'i'
        elif letter == 'q':
            s_list[index] = 'j'
        elif letter == 'p':
            s_list[index] = 'k'
        elif letter == 'o':
            s_list[index] = 'l'
        elif letter == 'n':
            s_list[index] = 'm'
        elif letter == 'm':
            s_list[index] = 'n'
        elif letter == 'l':
            s_list[index] = 'o'
        elif letter == 'k':
            s_list[index] = 'p'
        elif letter == 'j':
            s_list[index] = 'q'
        elif letter == 'i':
            s_list[index] = 'r'
        elif letter == 'h':
            s_list[index] = 's'
        elif letter == 'g':
            s_list[index] = 't'
        elif letter == 'f':
            s_list[index] = 'u'
        elif letter == 'e':
            s_list[index] = 'v'
        elif letter == 'd':
            s_list[index] = 'w'
        elif letter == 'c':
            s_
