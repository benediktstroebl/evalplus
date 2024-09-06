
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
    def shift_num(a,b):
        """create a function shift_num that takes in two arguments a
        and b where a is a string and b is a int.
        Return a string shifted by b places to the right.
        """
        temp = list(a)
        for i in range(len(a)):
            temp[i] = ord(temp[i]) - b
            if ord(temp[i]) < 65:
                temp[i] = chr(ord(temp[i]) + 26)
        return "".join(temp)
    a = []
    for i in range(len(s)):
        if s[i].isalpha():
            a.append(s[i])
    b = []
    for i in range(len(s)):
        if s[i].isalpha():
            b.append(ord(s[i]))
    c = []
    for i in range(len(a)):
        c.append(shift_num(a[i], b[i]))
    return "".join(c)

