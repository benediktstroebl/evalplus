
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
    result = ""
    for ch in s:
        # checking for lowercase letters and shifting them
        if ord(ch) >= 97 and ord(ch) <= 122:
            if ord(ch) >= 114:
                result += chr(ord(ch) + 2 - 26)
            else:
                result += chr(ord(ch) + 2)
        # checking for uppercase letters and shifting them
        elif ord(ch) >= 65 and ord(ch) <= 90:
            if ord(ch) >= 82:
                result += chr(ord(ch) + 2 - 26)
            else:
                result += chr(ord(ch) + 2)
        # adding unchanged characters to the output string
        else:
            result += ch

    return result
