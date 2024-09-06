
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
    result = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                if letter == 'Z':
                    result += 'A'
                else:
                    result += chr(ord(letter)+26*2)
            elif letter.islower():
                if letter == 'z':
                    result += 'a'
                else:
                    result += chr(ord(letter)+26*2)
        else:
            result += letter
    return result
