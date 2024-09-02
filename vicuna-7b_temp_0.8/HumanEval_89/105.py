
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
    new_string = ""
    for c in s:
        if c in string.ascii_lowercase:
            new_string += string.ascii_lowercase.index(c) * (ord(c) - 97) % 26
        else:
            new_string += string.ascii_uppercase.index(c) * (ord(c) - 64) % 26
    return new_string

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns the decrypted string using the encryption function above.
    """
    new_string = ""
    for c in s:
        if c in string.ascii_lowercase:
            new_string += string.ascii_lowercase.index(c) * (ord(c) + 97) % 26
        else:
            new_string += string.ascii_uppercase.index(c) * (ord(c) + 64) % 26
    return new_string

def encrypt_file(filename):
    """Encrypt the contents of a file using the encrypt function above.
    """
    with open(filename, "r") as file:
        encrypted_string = file.read()
    return encrypt(encrypted_string)

def decrypt_file(filename):
    """Decrypt the contents of a file using the decrypt function above.
    """
    with open(filename, "r") as file:
        decrypted_string = file.read()
    return decrypt(decrypted_string)
