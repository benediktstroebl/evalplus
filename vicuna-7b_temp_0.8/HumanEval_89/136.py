
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
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'b' or s[i] == 'c' or s[i] == 'd' or s[i] == 'e' or s[i] == 'f' or s[i] == 'g' or s[i] == 'h':
            s[i] += 'z'
        elif s[i] == 'j' or s[i] == 'k' or s[i] == 'l' or s[i] == 'm' or s[i] == 'n' or s[i] == 'o' or s[i] == 'p' or s[i] == 'q' or s[i] == 'r' or s[i] == 's' or s[i] == 't' or s[i] == 'u' or s[i] == 'v' or s[i] == 'w':
            s[i] += 'x'
        elif s[i] == 'y' or s[i] == 'z':
            s[i] += 'y'
    return s
