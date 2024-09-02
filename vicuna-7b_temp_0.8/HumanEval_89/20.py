
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
    # Get a list of all letters in the string
    letters = s.lower().split()
    
    # Initialize a variable to store the encrypted string
    encrypted = []
    
    # Loop through the letters in the string
    for letter in letters:
        # If the letter is in the alphabet, add it to the encrypted string
        if letter in alphabet:
            encrypted.append(letter)
        else:
            # Otherwise, add the letter in the correct position in the encrypted string
            if letter.isalpha():
                # If the letter is a vowel, add it in the correct position
                if 'aeiou' in letter:
                    encrypted.append(letter)
                else:
                    # If the letter is not a vowel, add it in the correct position
                    if letter.isdigit():
                        # If the letter is a digit, add it in the correct position
                        encrypted.append(chr(ord('a') - 2))
                    else:
                        # If the letter is not a digit, add it in the correct position
                        encrypted.append(chr(ord('b') - 2))
            else:
                # Add the letter in the correct position
                encrypted.append(letter)
    
    # Return the encrypted string
    return ''.join(encrypted)
