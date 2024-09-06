import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Args:
        text (str): The string to encrypt.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text:
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return None