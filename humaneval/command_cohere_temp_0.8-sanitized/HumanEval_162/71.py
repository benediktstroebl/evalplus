import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
    text (str): The input string to encrypt

    Returns:
    str or None: MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text: 
        return hashlib.md5(text.encode()).hexdigest() 
    else: 
        return None