
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
    encrypted = ""
    for i in range(0, len(s)):
        index = alphabet.find(s[i])
        if index == -1:
            encrypted += s[i]
        else:
            index += 1
            if index >= len(alphabet):
                index = index - len(alphabet)
            encrypted += alphabet[index]
    return encrypted
