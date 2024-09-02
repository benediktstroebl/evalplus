
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
    #This will be the place you store the new encrypted message
    encrypted_message = ''
    #This is used to access the elements of the string
    x = 0
    #This is used to create the rotation of the alphabet
    shift = 2
    #This is used to access the elements of the alphabet
    y = 0

    while x < len(s):
        #This will check that the current letter is in the alphabet
        if s[x] in 'abcdefghijklmnopqrstuvwxyz':
            #This will rotate the alphabet by the amount specified
            x = ord(s[x]) + shift
            if x > 122:
                #This is used to wrap around the alphabet
                x = x - 122

        #This will append the letter to the encrypted message
        encrypted_message += chr(x)
        #This will increase the index by 1
        x += 1

    return encrypted_message
