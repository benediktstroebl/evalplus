
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
    # Replace ' ' with '+' and '-' with '\_'
    s = s.replace(" ", "+")
    s = s.replace("-", "\_")
    
    # Initialize variables
    index = 0
    result = ""
    
    # Loop through characters in the string
    for char in s:
        # If the char is a digit, append it to the result
        if char.isdigit():
            result += char
        else:
            # If the char is a letter, add 10 to the index
            if char.isalpha():
                index += 10
                if index > 26:
                    index -= 26
                result += chr(ord("a") + index)
    
    return result
