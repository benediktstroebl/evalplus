
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = alphabet[2:12]
    b = alphabet[0:2]
    c = alphabet[13:25]
    d = alphabet[12:13]
    e = alphabet[25:28]
    f = alphabet[10:13]
    g = alphabet[9:10]
    h = alphabet[28:29]
    i = alphabet[29:30]
    j = alphabet[7:9]
    k = alphabet[6:7]
    l = alphabet[30:31]
    m = alphabet[31:32]
    n = alphabet[5:6]
    o = alphabet[4:5]
    p = alphabet[32:33]
    q = alphabet[33:34]
    r = alphabet[34:35]
    s = alphabet[3:4]
    t = alphabet[2:3]
    u = alphabet[1:2]
    v = alphabet[36:37]
    w = alphabet[0:1]
    x = alphabet[
