
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
    l=list(s)
    new=[]
    for i in l:
        if (ord(i)>=65 and ord(i)<=90):
            if (ord(i)+2)>90:
                new.append(chr(65+(ord(i)+2)-91))
            else:
                new.append(chr(ord(i)+2))
        elif (ord(i)>=97 and ord(i)<=122):
            if (ord(i)+2)>122:
                new.append(chr(97+(ord(i)+2)-123))
            else:
                new.append(chr(ord(i)+2))
    return ''.join(new)
