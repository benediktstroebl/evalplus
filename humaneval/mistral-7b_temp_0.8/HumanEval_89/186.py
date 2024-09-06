
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
    # Here you are going to need to use two loops, a for loop and a while loop
    # The for loop should iterate over each letter in the string
    # The while loop should check if the letter is a lower case letter
    # If the letter is a lower case letter then it should be replaced with the letter
    # If the letter is a upper case letter then it should be replaced with the letter
    # Rotate the string in a manner such that the letters shift down by two multiplied to two places.

    new_s = ''
    # for loop
    for i in s:
        # if loop
        if i.islower():
            new_s += chr((ord(i) + 13) % 26)
        elif i.isupper():
            new_s += chr((ord(i) + 13) % 26)
        else:
            new_s += i
    return new_s

