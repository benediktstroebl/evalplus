
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
    encrypted_word = ""
    for i in range(0, len(s)):
        if s[i] in alphabet:
            index = alphabet.index(s[i])
            new_index = index + 2
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += s[i]
    return encrypted_word
