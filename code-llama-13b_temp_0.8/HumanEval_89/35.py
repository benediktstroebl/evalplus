
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
    original_string = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = "ijklmnopqrstuvwxyzabcdefgh"
    encrypted_list = list(s)
    for i in range(len(s)):
        for j in range(len(original_string)):
            if s[i] == original_string[j]:
                encrypted_list[i] = encrypted_string[j]
    return ''.join(encrypted_list)

