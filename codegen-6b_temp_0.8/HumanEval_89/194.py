
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
    def digsub_encrypt(s):
        """Return the particular digit of s as if it were a positive integer."""
        return int(s)%26
    
    # "rotate" the alphabet:
    
    rotated_alphabet = []
    for i in range(26):
        rotated_alphabet.append(((i+1)%26)+1)
    
    # add in a number to denote the alphabet 'a' at the beginning:

    rotated_alphabet.insert(0, 0)
    
    # encrypt:
    
    encrypted_result = ''
    
    for letter in s:
        encrypted_result += rotated_alphabet[digsub_encrypt(letter)]
    
    return encrypted_result
