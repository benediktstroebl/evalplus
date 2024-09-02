
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
    num = int(input("Please input a number: "))
    count = 0
    temp = s
    for i in s:
        if i in "abcdefghijklmnopqrstuvwxyz":
            i = chr(ord(i) + num)
            count += 1
            print(i)
    print(temp)
    print(count)

