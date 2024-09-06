
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
    new_alphabet = list(alphabet)
    new_alphabet[0], new_alphabet[1], new_alphabet[2], new_alphabet[3] = new_alphabet[3], new_alphabet[2], new_alphabet[1], new_alphabet[0]
    encryption_key = chr(32 + len(alphabet) % 2) + chr(2 * len(alphabet) % 2)
    encrypted_string = ''
    for i in range(len(s)):
        encrypted_string += new_alphabet[ord(s[i]) // 2]
    return encryption_key + encrypted_string
