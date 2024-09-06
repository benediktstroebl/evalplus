import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Args:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input is empty.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()