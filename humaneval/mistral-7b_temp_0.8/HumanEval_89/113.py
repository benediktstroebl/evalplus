
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

    rotated_alpha = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alpha_2 = list("abcdefghijklmnopqrstuvwxyz")
    rotated_alpha_3 = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(rotated_alpha)):
        rotated_alpha[i] = chr(ord(rotated_alpha[i]) + 2 * 2)
    for i in range(len(rotated_alpha_2)):
        rotated_alpha_2[i] = chr(ord(rotated_alpha_2[i]) + 2 * 2 * 2)
    for i in range(len(rotated_alpha_3)):
        rotated_alpha_3[i] = chr(ord(rotated_alpha_3[i]) + 2 * 2 * 3)

    # rotated_alpha = list("abcdefghijklmnopqrstuvwxyz")
    # for i in range(len(
