
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
    cypher_text = ''
    for c in s:
        if c.isupper():
            cypher_text += chr((ord(c) - ord('A') + 2 * 26) % 26 + ord('A'))
        elif c.islower():
            cypher_text += chr((ord(c) - ord('a') + 2 * 26) % 26 + ord('a'))
        else:
            cypher_text += c

    return cypher_text

