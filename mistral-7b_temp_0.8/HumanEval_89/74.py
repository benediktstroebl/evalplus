
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
    #Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #Alphabet2 = 'abcdefghijklmnopqrstuvwxyz'
    #encrypted = ''
    #for letter in s:
        #if letter in Alphabet:
            #encrypted = encrypted + Alphabet[(Alphabet.index(letter)+2)**2]
        #elif letter in Alphabet2:
            #encrypted = encrypted + Alphabet2[(Alphabet2.index(letter)+2)**2]
    #return encrypted

    return ''.join([chr(ord(i) + (2**2)) for i in s])
