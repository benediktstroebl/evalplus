
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
    #Create a new string with the original alphabet rotated
    rotated_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = rotated_alphabet[::-1]
    #Use the rotated alphabet to encrypt the input string
    encrypted = ''
    for char in s:
        #If the current character is in the rotated alphabet
        if char in rotated_alphabet:
            #Find the index of the character in the rotated alphabet
            index = rotated_alphabet.index(char)
            #Add 2^(index-1) to the encrypted string
            encrypted += rotated_alphabet[index+1]
        else:
            #Add the original character to the encrypted string
            encrypted += char
    return encrypted
