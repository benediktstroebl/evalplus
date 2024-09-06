import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    For an empty string, returns None.

    Args:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 string or None for empty input.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()