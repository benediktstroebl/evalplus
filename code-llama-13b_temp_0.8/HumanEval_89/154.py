
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
    # Your code here
    str = s
    str_lst = list(str)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_lst = list(alphabet)
    alphabet_dict = {}
    # alph_dict = {'a':0, 'b':1, 'c':2 ... 'z':25}
    for i in range(len(alphabet_lst)):
        alphabet_dict[alphabet_lst[i]] = i
    # alph_dict = {'a':0, 'b':1, 'c':2 ... 'z':25}
    
    new_alphabet = alphabet_lst[2:] + alphabet_lst[:2]
    new_alphabet_lst = list(new_alphabet)
    # new_alph_dict = {'a':2, 'b':3, 'c':4 ... 'z':27}
    for i in range(len(new_alphabet_lst)):
        alphabet_dict[new_alphabet_lst[i]] = i + 2
    # alph_dict = {'a':0, 'b':1, 'c':2 ... 'z':25, 'A':26, 'B':27, 'C':28 ... 'Z':51}
    
    for i in range(len(str_lst)):
        if str_lst[i] in alphabet_dict:
            str_lst[i] = new_alphabet_lst[alphabet_dict[str_lst[i]] % 26]
    str = ''.join(str_lst)
    return str
