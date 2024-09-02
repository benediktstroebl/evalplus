
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
    encrypted_str=""
    for i in range(len(s)):
        char_to_encrypt=s[i]
        char_to_encrypt=char_to_encrypt.lower()
        index_in_alphabet=ord(char_to_encrypt)-97
        if index_in_alphabet+2>=len(encrypted_str):
            index_in_alphabet=(index_in_alphabet+2)-26
        encrypted_str=encrypted_str+chr(index_in_alphabet+97)
    return encrypted_str
