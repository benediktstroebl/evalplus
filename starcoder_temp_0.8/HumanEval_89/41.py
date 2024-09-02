
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
    a = alphabet[2:]
    b = alphabet[:2]
    c = a + b
    d = c[2:]
    e = d[:2]
    f = c + e
    g = f[2:]
    h = g[:2]
    i = f + h
    j = i[2:]
    k = j[:2]
    l = i + k
    m = l[2:]
    n = m[:2]
    o = l + n
    p = o[2:]
    q = p[:2]
    r = o + q
    s = r[2:]
    t = s[:2]
    u = t[2:]
    v = u[:2]
    w = t + v
    x = w[2:]
    y = x[:2]
    z = w + y
    q = z[2:]
    r = q[:2]
    a = r + z
    b = a[2:]
    c = b[:2]
    d = a + c
    e = d[2:]
    f = e[:2]
    g = d + f
    h = g[2:]
    i = h[:2]
    j = g + i
    k = j[2:]
    l = k[:2]
    m = j + l
    n = m[2:]
    o = n[:2]
    p = m + o
    q = p[2:]
    r = q[:2]
    s = r[2:]
    t = s[:2]
    u = t[2:]
    v = u[:2]
    w = t + v
    x = w[2:]
    y = x[:2]
    z = w + y
    alphabet = z
    s = s.lower()
    if isinstance(s, str):
        return "".join([alphabet[alphabet.index(l)] for l in s])
