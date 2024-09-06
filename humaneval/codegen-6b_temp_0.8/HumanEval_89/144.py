
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
    new_alphabet = alphabet[2:] + alphabet[0:2]
    new_alphabet_list = list(new_alphabet)
    new_alphabet_dict = dict(zip(alphabet, new_alphabet_list))

    def encrypt_fix(s):
        s = s.lower()
        out = ''
        for i in s:
            if i in alphabet: 
                out += new_alphabet_dict[i]
            else:
                out += i
        return out

    return encrypt_fix
