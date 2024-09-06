
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
    new_string = ""
    for letter in s:
        if letter == 'a':
            new_string = new_string + 'm'
        if letter == 'b':
            new_string = new_string + 'n'
        if letter == 'c':
            new_string = new_string + 'o'
        if letter == 'd':
            new_string = new_string + 'p'
        if letter == 'e':
            new_string = new_string + 'q'
        if letter == 'f':
            new_string = new_string + 'r'
        if letter == 'g':
            new_string = new_string + 's'
        if letter == 'h':
            new_string = new_string + 't'
        if letter == 'i':
            new_string = new_string + 'u'
        if letter == 'j':
            new_string = new_string + 'v'
        if letter == 'k':
            new_string = new_string + 'w'
        if letter == 'l':
            new_string = new_string + 'x'
        if letter == 'm':
            new_string = new_string + 'y'
        if letter == 'n':
            new_string = new_string + 'z'
        if letter == 'o':
            new_string = new_string + 'a'
        if letter == 'p':
            new_string = new_string + 'b'
        if letter == 'q':
            new_string = new_string + 'c'
        if letter == 'r':
            new_string = new_string + 'd'
        if letter == 's':
            new_string = new_string + 'e'
        if letter == 't':
            new_string = new_string + 'f'
        if letter == 'u':
            new_string = new_string + 'g'
        if letter == 'v':
            new_string = new_string + 'h'
        if letter == 'w':
            new_string = new_string + 'i'
        if letter == 'x':
            new_string = new_
