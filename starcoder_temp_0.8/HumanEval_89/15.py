
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
    s = s.lower()
    string_list = [x for x in s]
    ans = ""
    for i in range(len(string_list)):
        if string_list[i].isalpha():
            alpha_index = ord(string_list[i]) - 97
            alpha_index = alpha_index - 2
            alpha_index = alpha_index + (26*2)
            alpha_index = alpha_index % 26
            alpha_index = alpha_index + 97
            ans += chr(alpha_index)
        else:
            ans += string_list[i]
    return ans

