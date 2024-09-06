
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
    # write your code here
    encypt_message=""
    for char in s:
        if char.isupper():
            ascii_value=ord(char)
            encypt_message+=chr((ascii_value+40)%90+32)
        elif char.islower():
            ascii_value=ord(char)
            encypt_message+=chr((ascii_value+40)%122+97)
        else:
            encypt_message+=char
    return encypt_message
