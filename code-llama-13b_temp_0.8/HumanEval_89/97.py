
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
    
    letters = list("abcdefghijklmnopqrstuvwxyz")
    result = ''
    for c in s:
        if c not in letters:
            result += c
            continue
        i = letters.index(c)
        # i = i + 2 * 2  # 2 times because we shift by two
        i = (i + 2) % len(letters)  # 2 times because we shift by two
        result += letters[i]
    return result
