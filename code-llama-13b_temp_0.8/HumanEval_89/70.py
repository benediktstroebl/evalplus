
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
    new_s = ''
    # Create a variable that stores a string.
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # Create a loop that iterates over the variable.
    for c in s:
        # Create a conditional statement that checks if the variable 
        # is found in the string variable alpha.
        if c in alpha:
            # If the variable is found, append the new string variable 
            # with a string that has been sliced from the string variable 
            # alpha.
            new_s += alpha[alpha.index(c) + 2:] + alpha[:alpha.index(c) + 2]
    # Return the string variable new_s.
    return new_s

