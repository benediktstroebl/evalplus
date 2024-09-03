def encrypt(s):
    """Create a function to encrypt a string using a custom rotation scheme.
    Encryption scheme: shifts all letters down by twice and returns the rotated string.
    Args: 
        - string s to encrypt 
    Returns: 
        - the encrypted string
    """
    alphabet = 'abcdefghijklmnopqr'
    rotated_alphabet = [c[2:] + c[0] for c in alphabet]
    return ''.join(rotated_alphabet, s)