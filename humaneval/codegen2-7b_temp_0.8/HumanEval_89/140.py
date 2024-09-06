
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
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = alphabet.find(s[0])
    s = s[1:]
    encrypted_list = [alphabet[(alphabet.find(s[0])+num)%26]+s[1:] for s in s]
    encrypted_string = ''.join(encrypted_list)
    return encrypted_string

