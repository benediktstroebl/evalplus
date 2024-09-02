
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
    n = len(s)
    p = [[0 for j in range(26)] for i in range(n)]
    for i in range(n):
        p[i][s[i] - 'a'] += 1
    for i in range(n):
        p[i][s[i] - 'a'] += 1
    p[n-1][n-1] -= 2
    r = ''
    for i in range(n-1, -1, -1):
        for j in range(26):
            if p[i][j] > 0:
                r += chr(j + (p[i][j] - 1) % 26)
        r += chr(n-i-1)
    return r
