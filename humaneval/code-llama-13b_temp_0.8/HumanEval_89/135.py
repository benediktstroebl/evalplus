
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
    # create alphabet
    alph = "abcdefghijklmnopqrstuvwxyz"
    
    # find shift
    shift = 2 * 2
    
    # list to store the encrypted string
    new_s = []
    
    # iterate through the string
    for i in s:
        # if the character is not in the alphabet, just append to the new list
        if i not in alph:
            new_s.append(i)
        else:
            # find the index of the character
            idx = alph.index(i)
            # get the new index
            new_idx = (idx + shift) % len(alph)
            # get the new character
            new_i = alph[new_idx]
            # append to the new string
            new_s.append(new_i)
            
    # convert the list into a string
    new_s = ''.join(new_s)
    return new_s
    
