import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string into MD5 and returns the result.
    For an empty string, returns None.

    Args:
        text (str): The string to encrypt.

    Returns:
        str or None: The MD5 hash of the input string or None if the input is empty.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()