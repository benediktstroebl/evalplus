
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
    final = ''
    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            char_lower = char.lower()
            if char_lower.isupper():
                char_lower = char_lower.lower()
            lower_code = ord(char_lower)
            upper_code = ord(char)
            new_code = 65 + ((upper_code - 65) * 2 * 2)
            if char_lower.islower():
                char = chr(new_code)
                final += char
            elif char_lower.isupper():
                char = chr(new_code)
                final += char.upper()
        else:
            final += char
    return final









































































