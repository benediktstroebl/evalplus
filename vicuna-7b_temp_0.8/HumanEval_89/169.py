
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
    string = s + 'kj'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while i < len(string) - 2:
        j = i + 1
        while j < len(string) - 2 and alphabet[string[i]] <= alphabet[string[j]]:
            j += 1
        if j > i:
            string = string[:i] + string[j:]
            i = j
    return string

