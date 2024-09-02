
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
    #rotate = "abcdefghijklmnopqrstuvwxyz".upper()
    # return "".join([rotate[(rotate.index(l) + 2) % 26] for l in s])
    # alternate solution:
    shift_matrix = [""] * 26
    for i in range(26):
        shift_matrix[i] = chr(ord('A') - 2 + i)
    shift_matrix = "".join(shift_matrix)
    return "".join([shift_matrix.index(l) for l in s])


