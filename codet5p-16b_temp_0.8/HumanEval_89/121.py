
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

    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_2 = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    
    for i in range(len(alphabet)):
        if s[0] == alphabet[i]:
            alphabet_2[i] = s[0]
            break
    for i in range(len(alphabet)):
        if s[1] == alphabet[i]:
            alphabet_2[i] = s[1]
            break
    for i in range(len(alphabet)):
        if s[2] == alphabet[i]:
            alphabet_2[i] = s[2]
            break
    for i in range(len(
