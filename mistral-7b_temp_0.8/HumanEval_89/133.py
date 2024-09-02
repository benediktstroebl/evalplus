
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
    r = int(input("enter the rotation number:"))
    string=input("Enter the String:")
    if(r<0):
        r*=(-1)
    z = string
    for i in range(len(z)):
        if(z[i].isupper()):
            z = z.replace(z[i],chr(ord(z[i])-r))
        elif(z[i].islower()):
            z = z.replace(z[i],chr(ord(z[i])+r))
        else:
            pass
    print(z)

