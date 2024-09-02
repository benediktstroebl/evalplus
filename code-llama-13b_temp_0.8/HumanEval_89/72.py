
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
    for c in s:
        char_num = ord(c)
        # check if lowercase letter
        if char_num >= 97 and char_num <= 122:
            # 122 = ord('z')
            if (char_num + 4) > 122:
                char_num = 96 + (char_num + 4 - 123)
            else:
                char_num += 4
        # check if uppercase letter
        elif char_num >= 65 and char_num <= 90:
            # 90 = ord('Z')
            if (char_num + 4) > 90:
                char_num = 64 + (char_num + 4 - 91)
            else:
                char_num += 4
        result += chr(char_num)
    return result
