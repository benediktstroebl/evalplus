
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
    
    # creating dictionary of letter:letter encoding
    letter_dict = {}
    for i in range(len(alphabet)):
        letter_dict[alphabet[i]] = alphabet[(i+2)%len(alphabet)]
        
    # creating string to be encrypted
    encrypted_string = ""
    for c in s:
        if c == " ":
            encrypted_string += " "
        else:
            encrypted_string += letter_dict[c]
    return encrypted_string
