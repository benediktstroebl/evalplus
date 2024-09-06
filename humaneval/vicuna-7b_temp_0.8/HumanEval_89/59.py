
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
    alphabets=['abcdefghijklmnopqrstuvwxyz']
    encrypted_string=[]
    for char in s:
        if char.isalpha():
            i=ord(char) - ord('a')
            if i > 19:
                i = i % 26
            if i == 0:
                i = 26
            encrypted_string.append(alphabets[i])
        else:
            encrypted_string.append(char)
    return ''.join(encrypted_string)
