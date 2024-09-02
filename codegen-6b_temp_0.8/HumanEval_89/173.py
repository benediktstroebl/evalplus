
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
    new_alphabet = alphabet[1:] + alphabet[0]
    new_alphabet = new_alphabet[1:] + new_alphabet[0]
    new_alphabet = new_alphabet[3:] + new_alphabet[:3]
    new_alphabet = new_alphabet[3:] + new_alphabet[:3]
    new_alphabet = new_alphabet[1:] + new_alphabet[:1]
    new_alphabet = new_alphabet[1:] + new_alphabet[:1]
    new_alphabet = new_alphabet[3:] + new_alphabet[:3]
    new_alphabet = new_alphabet[3:] + new_alphabet[:3]
    new_alphabet = new_alphabet[1:] + new_alphabet[:1]
    rotated_alphabet = alphabet[3:] + alphabet[:3]
    
    def encrypt_new(s):
        s = s.lower()
        for char in s:
            if char not in alphabet:
                return s
            if char in alphabet:
                s = s.replace(char, rotated_alphabet[alphabet.index(char)])
        return s
    return encrypt_new(s)
