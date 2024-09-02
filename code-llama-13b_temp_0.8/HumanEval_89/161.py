
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    dict_letters = {}
    for i in range(len(letters)):
        if (i + 2) < 26:
            dict_letters[letters[i]] = letters[i + 2]
        else:
            dict_letters[letters[i]] = letters[i - 24]

    new_s = ''
    for i in range(len(s)):
        if s[i].lower() in dict_letters:
            new_s += dict_letters[s[i].lower()].upper() if s[i].isupper() else dict_letters[s[i].lower()]
        else:
            new_s += s[i]

    return new_s
