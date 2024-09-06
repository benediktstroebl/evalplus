
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
    alphabet += alphabet.upper()
    alphabet +=''
    new_s = ''
    for i in s:
        if i in alphabet:
            index = alphabet.find(i)
            index += 2*2
            new_s += alphabet[index]
        else:
            new_s += i
    return new_s
