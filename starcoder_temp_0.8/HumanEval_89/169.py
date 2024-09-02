
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
    r = ""
    for i in s:
        if i.isalpha():
            if ord(i) - 97 >= 0 and ord(i) - 97 <= 25:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 26 and ord(i) - 97 <= 51:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 52 and ord(i) - 97 <= 77:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 78 and ord(i) - 97 <= 103:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 104 and ord(i) - 97 <= 129:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 130 and ord(i) - 97 <= 155:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 156 and ord(i) - 97 <= 181:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 182 and ord(i) - 97 <= 207:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 208 and ord(i) - 97 <= 233:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 234 and ord(i) - 97 <= 259:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 260 and ord(i) - 97 <= 285:
                r += chr(ord(i) + 10)
            elif ord(i) - 97 >= 286 and ord(i
