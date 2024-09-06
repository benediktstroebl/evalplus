
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
    decrypted = []
    for char in s:
        if char.isdigit():
            decrypted.append(int(char))
        else:
            index = alphabet.index(char)
            decrypted.append(alphabet[index+2*len(alphabet)//2])
    return ''.join(decrypted)
