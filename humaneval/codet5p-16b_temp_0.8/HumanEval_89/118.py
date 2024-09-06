
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
    letter1 = alphabet[2:] + alphabet[:2]
    letter2 = alphabet[:26] + alphabet[26:]
    letter3 = alphabet[26:] + alphabet[:26]
    output = ''
    for i in range(len(s)):
        current = s[i]
        if current.isalpha():
            if current.isupper():
                output += letter1[alphabet.index(current)].upper()
            else:
                output += letter1[alphabet.index(current)]
        else:
            output += current
    return output

