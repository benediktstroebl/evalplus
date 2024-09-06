
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
    letters = [chr(i) for i in range(65, 91)]
    letters.extend([chr(i) for i in range(97, 123)])
    
    letters_encrypt = []
    for letter in letters:
        index = letters.index(letter)
        index += 4
        if index >= 52:
            index -= 52
        letters_encrypt.append(letters[index])
    
    letters_encrypt_dict = {}
    for i in range(len(letters)):
        letters_encrypt_dict[letters[i]] = letters_encrypt[i]
    
    result = []
    for i in s:
        if i.isalpha():
            result.append(letters_encrypt_dict[i])
        else:
            result.append(i)
            
    return ''.join(result)
    
