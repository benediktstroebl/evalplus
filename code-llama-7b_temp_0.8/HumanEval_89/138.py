
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
    output_string = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                #the letters are shifted down by two multiplied to two places, from A-Z.
                output_string += chr(ord('A')+(ord(char)-ord('A')+2*2)%26)
            else:
                output_string += chr(ord('a')+(ord(char)-ord('a')+2*2)%26)
        else:
            output_string += char
    return output_string
