
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
    
    encrypted_string = ''
    for char in s:
        if char in string.ascii_lowercase:
            index = (alphabet.index(char) - 2) % 26
            encrypted_string += alphabet[index]
        else:
            encrypted_string += char
    return encrypted_string
