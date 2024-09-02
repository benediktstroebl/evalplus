
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
    # my solution
    return ''.join([chr(ord(c) + 2 * 2) if ord(c) < 122 else chr(ord(c) + (2 * 2) - 26) for c in s])
    # more pythonic
    return ''.join([chr(ord(c) + 2 * 2 - 26) if ord(c) > 121 else chr(ord(c) + 2 * 2) for c in s])
    # r1eally pythonic
    # return s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'))

    # def rotate(word):
    #     result = ''
    #     for i in word:
    #         if ord(i) == 122:
    #             result += 'a'
    #         elif ord(i) == 121:
    #             result += 'z'
    #         else:
    #             result += chr(ord(i) + 2)
    #     return result
    # return rotate(rotate(s))
    # return s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'))

