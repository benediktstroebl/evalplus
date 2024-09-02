
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
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'aeybtmbnqkrsdcfoylpjhgfzx'
    for char in s:
        if char.isalpha():
            if char.lower() in a:
                # Encrypt the character
                e = chr(ord(char) + 27)
                if e not in b:
                    return e
        else:
            if char.isdigit():
                # Encrypt the number
                if char.isdigit():
                    # Convert the string to a float
                    n = float(s)
                    # Convert the float to a number
                    e = str(n)
                    # Shift the digits one step to the right
                    e = e[:-2] + e[2:] + e[:-2] + e[2:]
                    if e in b:
                        return e
                else:
                    # Convert the string to a float
                    n = float(s)
                    # Convert the float to a number
                    e = str(n)
                    # Shift the digits one step to the right
                    e = e[:-2] + e[2:] + e[:-2] + e[2:]
                    if e in b:
                        return e
    return ''