
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
    # your code
    result = ""
    for ch in s:
        if ch == " ":
            result += " "
            continue
        if ch.islower():
            ch = ord(ch)+2
            ch = chr(ch % 26 + ord('a'))
        elif ch.isupper():
            ch = ord(ch)+2
            ch = chr(ch % 26 + ord('A'))
        result += ch
    return result

