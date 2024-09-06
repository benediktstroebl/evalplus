
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
    new_alphabet = [alphabet[i] for i in range(len(alphabet)) for j in range(i+1, len(alphabet))]
    for i in range(len(s)):
        if s[i] in new_alphabet:
            index = [j for j in range(len(new_alphabet)) if new_alphabet[j] == s[i]][0]
            s = s[:i] + s[index] + s[i+1:]
    return s
