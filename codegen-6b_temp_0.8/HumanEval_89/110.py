
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
    
    # Create a dictionary of characters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shiftedAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Shift the alphabet forward or backwards depending on whether it is a negative or positive shift
    for i in range(0, len(alphabet)):
        if i is 0:
            shiftedAlphabet[i] = alphabet[len(alphabet) - 1]
        elif i is len(alphabet) - 1:
            shiftedAlphabet[i] = alphabet[0]
        else:
            shiftedAlphabet[i] = alphabet[i + 1]
            shiftedAlphabet[i] = shiftedAlphabet[i] + alphabet[i - 1]
    # Create a dictionary of the alphabet
    alphaDict = {}
    for i, val in enumerate(alphabet):
        alphaDict[val] = i
    
    # Create the encrypted string
    encryptedString = ''
    for character in s:
        if character is ' ':
            encryptedString = encryptedString + character
        elif character is ' ':
            pass
        else:
            encryptedString = encryptedString + shiftedAlphabet[alphaDict[character] - 2]
    return encryptedString
            