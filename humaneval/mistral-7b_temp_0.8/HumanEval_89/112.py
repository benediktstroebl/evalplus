
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
    # Encrypt a string
    # Your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot = 2 * 2
    a = ""
    for i in s:
        if i in alphabet:
            pos = alphabet.find(i)
            npos = pos + rot
            npos = npos % len(alphabet)
            n = alphabet[npos]
            a += n
        else:
            a += i
    return a

