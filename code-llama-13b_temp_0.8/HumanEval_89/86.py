
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
    s1 = []
    s1[:0] = s
    s2 = []
    for i in s1:
        if i == " ":
            s2.append(i)
        elif i.isupper():
            s2.append(chr((ord(i) - ord('A') + 2) % 26 + ord('A')))
        elif i.islower():
            s2.append(chr((ord(i) - ord('a') + 2) % 26 + ord('a')))
    return "".join(s2)

