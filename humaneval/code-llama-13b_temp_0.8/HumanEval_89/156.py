
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
    list_string = list(s)
    result = ''
    for i in list_string:
        if i.isupper():
            number = ord(i) + 2 * 26
            if number > ord('Z'):
                number = number - ord('Z') + ord('A') -1
            result += chr(number)
        elif i.islower():
            number = ord(i) + 2 * 26
            if number > ord('z'):
                number = number - ord('z') + ord('a') - 1
            result += chr(number)
        else:
            result += i
    return result
