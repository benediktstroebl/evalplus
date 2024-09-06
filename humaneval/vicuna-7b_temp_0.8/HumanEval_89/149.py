
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

    #Create a dictionary that maps characters to their corresponding
    #rotated position in the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = dict(zip(alphabet, alphabet[1:]))

    #Create a new string that will hold the encrypted value
    encrypted = ''

    #Iterate through each character in the input string
    for c in s:
        #If the character is not a letter
        if c not in alphabet:
            encrypted += c
        #If the character is a letter, add the rotated position of the
        #letter to the encrypted string and continue the loop
        else:
            encrypted += alphabet_rotated[c]
    
    return encrypted
