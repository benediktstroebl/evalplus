
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
    new_alphabet = list(alphabet)
    new_alphabet[0], new_alphabet[1], new_alphabet[2], new_alphabet[3] = new_alphabet[3], new_alphabet[2], new_alphabet[1], new_alphabet[0]
    for i in range(len(s)):
        if s[i] == 'a':
            s = s.replace(s[i], 'z')
        elif s[i] == 'b':
            s = s.replace(s[i], 'y')
        elif s[i] == 'c':
            s = s.replace(s[i], 'w')
        elif s[i] == 'd':
            s = s.replace(s[i], 'v')
        elif s[i] == 'e':
            s = s.replace(s[i], 'u')
        elif s[i] == 'f':
            s = s.replace(s[i], 't')
    return s
