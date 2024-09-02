
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
    # replace with your code
    def actualencrypt(s):
        newstring = ''
        for letter in s:
            if letter.isalpha():
                x = ord(letter) - 96
                y = (x + 2) % 26
                new = y + 96
                newletter = chr(new)
                newstring += newletter
            else:
                newstring += letter
        return newstring

    return actualencrypt(s)
    
    
