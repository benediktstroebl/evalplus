
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
    def rotational_cipher(s):
        """Rotates the alphabet in a way that will shift the letters down by 
        two for every letter, adding a space to the end.
        """
        alph = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s)
        for i in range(len(s)):
            s[i] = alph[(alph.find(s[i]) + (len(alph)//2)) % len(alph)]
        return ''.join(s)

    def rotational_cipher_alt(s):
        """Rotates the alphabet in a way that will shift the letters down by 
        two for every letter, adding a space to the end.
        """
        orig = 'abcdefghijklmnopqrstuvwxyz'
        new = 'zyxwvutsrqponmlkjihgfedcba'   
        return ''.join([new[x] for x in orig.upper().replace(orig, '').findall(s.upper())])

    return rotational_cipher_alt(s)


    
