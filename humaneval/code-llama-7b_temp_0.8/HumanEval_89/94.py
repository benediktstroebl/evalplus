
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
    s_list = list(s)
    new_list = []
    for char in s_list:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_list.append(chr(ord(char) - 64))
            continue
        if char in "abcdefghijklmnopqrstuvwxyz":
            new_list.append(chr(ord(char) - 96))
            continue
        else:
            new_list.append(char)
    new_list = [chr(ord(i) + 2) if ord(i) + 2 <= 122
                else chr(ord(i) - 26 + 97) for i in new_list]
    return "".join(new_list)

