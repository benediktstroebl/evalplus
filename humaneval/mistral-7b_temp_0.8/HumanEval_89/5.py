
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

    charList = []
    for i in s:
        charList.append(i)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numList = [x for x in range(26)]

    rotate = 2 ** 2

    for i in numList:
        i = i + rotate

    for i in numList:
        alphabet = alphabet[i:] + alphabet[:i]

    encrypt = ""
    for i in charList:
        if i in alphabet:
            encrypt += alphabet[alphabet.find(i)]
        else:
            encrypt += i

    return encrypt


