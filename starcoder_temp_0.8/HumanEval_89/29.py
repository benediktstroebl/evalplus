
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
    # your code here
    x = s.replace('a','z')
    y = x.replace('b','a')
    z = y.replace('c','b')
    w = z.replace('d','c')
    u = w.replace('e','d')
    v = u.replace('f','e')
    o = v.replace('g','f')
    p = o.replace('h','g')
    q = p.replace('i','h')
    r = q.replace('j','i')
    t = r.replace('k','j')
    y = t.replace('l','k')
    u = y.replace('m','l')
    i = u.replace('n','m')
    o = i.replace('o','n')
    p = o.replace('p','o')
    q = p.replace('q','p')
    r = q.replace('r','q')
    t = r.replace('s','r')
    y = t.replace('t','s')
    u = y.replace('u','t')
    i = u.replace('v','u')
    o = i.replace('w','v')
    p = o.replace('x','w')
    q = p.replace('y','x')
    r = q.replace('z','y')
    return r
