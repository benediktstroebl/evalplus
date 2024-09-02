
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = list(alphabet)
    string = list(s)
    string_final = []
    for i in string:
        for j in range(0,26):
            if i == alphabet_list[j]:
                string_final.append(alphabet_list[j+2])
    string_final_string = "".join(string_final)
    return string_final_string
