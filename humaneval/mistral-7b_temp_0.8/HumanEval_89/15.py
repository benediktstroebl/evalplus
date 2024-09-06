
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
    encrypted=""
    for i in s:
        if i=='a':
            encrypted+='b'
        elif i=='b':
            encrypted+='c'
        elif i=='c':
            encrypted+='d'
        elif i=='d':
            encrypted+='e'
        elif i=='e':
            encrypted+='f'
        elif i=='f':
            encrypted+='g'
        elif i=='g':
            encrypted+='h'
        elif i=='h':
            encrypted+='i'
        elif i=='i':
            encrypted+='j'
        elif i=='j':
            encrypted+='k'
        elif i=='k':
            encrypted+='l'
        elif i=='l':
            encrypted+='m'
        elif i=='m':
            encrypted+='n'
        elif i=='n':
            encrypted+='o'
        elif i=='o':
            encrypted+='p'
        elif i==
