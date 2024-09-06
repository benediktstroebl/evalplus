
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

    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha2 = alpha[2:] + alpha[:2]
    ans = ''
    for i in s:
        if i.isalpha():
            i = i.lower()
            if i not in alpha2:
                ans += i
            else:
                ind = alpha2.index(i)
                ans += alpha[ind]
        else:
            ans += i
    return ans

