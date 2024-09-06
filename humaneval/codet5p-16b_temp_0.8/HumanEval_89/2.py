
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_alphabet = s.replace(' ', '')
    new_alphabet = ''
    for letter in alphabet:
        if letter not in s_alphabet:
            new_alphabet += letter
        elif letter in s_alphabet:
            new_alphabet += letter
    print(new_alphabet)
    result = ''
    for i in range(len(s)):
        result += new_alphabet[(ord(s[i]) - 97) * 2 - 26]
    return result
