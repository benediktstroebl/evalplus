
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
    s = s.replace(' ','')
    for k in range(0,len(s)):
        if s[k] == 'a':
            s = s.replace('a','z')
        if s[k] == 'z':
            s = s.replace('z','a')
    s = s.replace('a','b')
    s = s.replace('b','c')
    s = s.replace('c','d')
    s = s.replace('d','e')
    s = s.replace('e','f')
    s = s.replace('f','g')
    s = s.replace('g','h')
    s = s.replace('h','i')
    s = s.replace('i','j')
    s = s.replace('j','k')
    s = s.replace('k','l')
    s = s.replace('l','m')
    s = s.replace('m','n')
    s = s.replace('n','o')
    s = s.replace('o','p')
    s = s.replace('p','q')
    s = s.replace('q','r')
    s = s.replace('r','s')
    s = s.replace('s','t')
    s = s.replace('t','u')
    s = s.replace('u','v')
    s = s.replace('v','w')
    s = s.replace('w','x')
    s = s.replace('x','y')
    s = s.replace('y','z')
    return s
