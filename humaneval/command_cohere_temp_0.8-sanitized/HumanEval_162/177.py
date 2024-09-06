import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if input is empty.
    """

    if not text:
        return None

    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest()