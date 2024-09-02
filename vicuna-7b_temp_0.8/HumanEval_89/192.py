
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
    new_alphabet = [chr(i + 27) for i in range(26)]
    result = ''
    for char in s:
        index = ord(char) - 97
        result = result + new_alphabet[index]
    return result

if **name** == '**main**':
    # Encrypting a string
    s = input("Enter a string to encrypt: ")
    encrypted_string = encrypt(s)
    print("Encrypted string: ", encrypted_string)
