
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
    # Replace the dictionary with a list and sort it
    alphabet = sorted(string.ascii_uppercase)
    
    # Start with a empty string
    encrypted = ""
    
    # Loop through the string
    for i in range(len(s)):
        # Move to the next letter
        next_letter = alphabet[i]
        
        # If the letter is the last letter of the string
        if i == len(s) - 1:
            # Copy the rest of the encrypted string to the next letter
            next_letter = encrypted + next_letter
        else:
            # Copy the rest of the encrypted string to the next letter
            next_letter = encrypted[:-1]
        # Append the encrypted letter
        encrypted += next_letter
    return encrypted
