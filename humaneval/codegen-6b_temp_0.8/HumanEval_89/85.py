
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

    x = [0] * 26
    y = [0] * 26

    for i in range(len(alphabet)):
        x[i] = alphabet[i]
        y[i] = alphabet[(i + 2) % 26]

    # print(x)
    # print(y)

    # print(alphabet[-1])
    # print(alphabet[-2])

    # print(alphabet[-3])
    # print(alphabet[-4])

    z = [0] * 26

    for i in range(len(s)):
        # print(s[i])
        # print(alphabet.index(s[i]))
        z[alphabet.index(s[i])] = y[alphabet.index(s[i])]

    e = ''
    for i in range(len(z)):
        e += z[i]
    # print(e)
    return e

