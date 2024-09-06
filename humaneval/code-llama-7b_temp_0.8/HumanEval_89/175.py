
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
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS = LETTERS*2
    LETTERS2 = LETTERS2*2
    LETTERS = LETTERS[2:] + LETTERS[:2]
    LETTERS2 = LETTERS2[2:] + LETTERS2[:2]
    translated = ''
    i = 0
    while i < len(s):
        if s[i] in LETTERS:
            # if LETTERS.index(s[i]) >= 8:
            #     translated += LETTERS2[i - 1]
            # else:
                translated += LETTERS2[LETTERS.index(s[i])]
            i += 1
        else:
            translated += s[i]
            i += 1
    return translated

