
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
    if len(s)%2 == 1:
        s += 'x'
    encrypted_str = ''
    for i in range(len(s)):
        ascii = ord(s[i])
        if ascii >= 97 and ascii <= 122:
            if ascii + 24 >= 123:
                ascii += 24
            else:
                ascii += 24
        else:
            ascii += 24
        encrypted_str += chr(ascii)
    return encrypted_str

