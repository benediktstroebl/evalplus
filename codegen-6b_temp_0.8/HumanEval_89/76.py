
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
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    encrypt = ''
    for i in s:
        if i.isalpha():
            num = s.index(i)
            if num == 26:
                num = 0
            elif num == 27:
                num = 1
            elif num == 28:
                num = 2
            elif num == 29:
                num = 3
            elif num == 30:
                num = 4
            elif num == 31:
                num = 5
            elif num == 32:
                num = 6
            elif num == 33:
                num = 7
            elif num == 34:
                num = 8
            elif num == 35:
                num = 9
            elif num == 36:
                num = 10
            elif num == 37:
                num = 11
            elif num == 38:
                num = 12
            elif num == 39:
                num = 13
            elif num == 40:
                num = 14
            elif num == 41:
                num = 15
            elif num == 42:
                num = 16
            elif num == 43:
                num = 17
            elif num == 44:
                num = 18
            elif num == 45:
                num = 19
            elif num == 46:
                num = 20
            elif num == 47:
                num = 21
            elif num == 48:
                num = 22
            elif num == 49:
                num = 23
            elif num == 50:
                num = 24
            elif num == 51:
                num = 25
            num = num + 2
            
            encrypt = encrypt + alpha[num]
        else:
            encrypt = encrypt + i
        
    return encrypt
