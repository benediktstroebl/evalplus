
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
    cipher = alphabet[2:] + alphabet[:2]
    # A = 'A'
    # B = 'B'
    # cipher = B + A

    # for i in range(2):
    #     cipher += alphabet[0]

    # cipher += alphabet[:2]
    # cipher = alphabet[2:] + alphabet[:2]

    # return ''.join([cipher[ord(i) - 97] for i in s])
    # return ''.join([cipher[ord(i) - 97] for i in s])
    return ''.join([cipher[ord(i) - 97] for i in s])

