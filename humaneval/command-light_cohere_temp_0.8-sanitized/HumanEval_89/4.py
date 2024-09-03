def encrypt(s):
    """Create a function to encrypt a string with the alphabet rotated.
    alphabet shift is down two places.

    Args: 
        s (strring string)
        
    Returns: 
        encrypted string
    """
    s = ''.join(s)
    return s[::2]