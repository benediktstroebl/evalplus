
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
    result = ''
    for i in s:
        # Checks if the character is a lowercase letter
        if 'a' <= i <= 'z':
            # Asci code
            num = ord(i) - 95
            # To make sure it wraps around
            num = num % 26 + 2
            num = num * 2
            result += chr(num + 96)
        # Checks if the character is an uppercase letter
        elif 'A' <= i <= 'Z':
            # Asci code
            num = ord(i) - 64
            # To make sure it wraps around
            num = num % 26 + 2
            num = num * 2
            result += chr(num + 64)
        # If character is not a letter
        else:
            result += i
    return result

