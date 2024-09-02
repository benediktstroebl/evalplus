
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
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    alphabet_two = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']
    for i in range(26):
        alphabet_two[i].append(alphabet[i])
        alphabet_two[i].append(alphabet_two[i])
        alphabet_two[i].append(alphabet_two[i])
        alphabet_two[i].append(alphabet_two[i])
        alphabet_two[i].append(alphabet_two[i])
    for i in range(26):
        alphabet_two[i].remove(alphabet[i])
        alphabet_two[i].remove(alphabet[i])
        alphabet_two[i].remove(alphabet[i])
        alphabet_two[i].remove(alphabet[i])
    for i in range(26):
        alphabet_two[i].remove(alphabet_two[i][0])
        alphabet_two[i].remove(alphabet_two[i][0])
        alphabet_two[i].remove(alphabet_two[i][0])
        alphabet_two[i].remove(alphabet_two[i][0])
    for i in range(26):
        alphabet_two[i] = alphabet_two[i][1:] + [alphabet_two[i][0]]
    for i in range(26):
        alphabet_two[i] = alphabet_two[i][2:] + [alphabet_two[i][0]]
