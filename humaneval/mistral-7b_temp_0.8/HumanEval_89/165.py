
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    def rotation(l):
        if l == 'a':
            return 'c'
        elif l == 'b':
            return 'd'
        elif l == 'c':
            return 'e'
        elif l == 'd':
            return 'f'
        elif l == 'e':
            return 'g'
        elif l == 'f':
            return 'h'
        elif l == 'g':
            return 'i'
        elif l == 'h':
            return 'j'
        elif l == 'i':
            return 'k'
        elif l == 'j':
            return 'l'
        elif l == 'k':
            return 'm'
        elif l == 'l':
            return 'n'
        elif l == 'm':
            return 'o'
        elif l == 'n':
            return 'p'
        elif l == 'o':
            return 'q'
        elif l == 'p':
            return 'r'
        elif l ==
