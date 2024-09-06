
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
    result = ""
    alphabet = [chr(i) for i in range(97, 123)]
    shift = 2
    for i in s:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += i
    return result

