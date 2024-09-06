
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
    new_alphabet = alphabet[len(alphabet) - 2:] + alphabet[:-2]
    new_alphabet = list(new_alphabet)
    new_alphabet[ord('j') - ord('a')] = 'a'
    new_alphabet[ord('z') - ord('a')] = 'z'
    new_alphabet[ord('k') - ord('a')] = 'b'
    new_alphabet[ord('t') - ord('a')] = 't'
    new_alphabet[ord('u') - ord('a')] = 't'
    new_alphabet[ord('v') - ord('a')] = 'x'
    new_alphabet[ord('w') - ord('a')] = 'y'
    new_alphabet[ord('y') - ord('a')] = 'y'
    new_alphabet[ord('x') - ord('a')] = 'x'
    new_alphabet[ord('z
