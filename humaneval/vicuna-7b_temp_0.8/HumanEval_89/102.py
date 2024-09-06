
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
    # Create an empty string to store the encrypted string
    encrypted = ""
    
    # Iterate over each character in the input string
    for c in s:
        # If the character is not a letter, append it to the encrypted string
        if c.isalpha():
            encrypted += c
        else:
            # If the character is not a letter, rotate the alphabet and append the result
            if c in "aeiou":
                # Add the unrotated character to the end of the alphabet
                # and add the unrotated character to the beginning of the rotated alphabet
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                rotated_alphabet = alphabet[0:len(alphabet)] + alphabet[len(alphabet)-1:]
                rotated_c = alphabet[rotated_alphabet.index(c)+1]
                # Append the rotated character to the encrypted string
                encrypted += rotated_c
            else:
                # Append the character to the encrypted string
                encrypted += c
    
    # Return the encrypted string
    return encrypted