import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    Returns None if the input string is empty.

    Args:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input string is empty.
    """
    if text and text.strip():
        # Use hashlib to generate MD5 hash
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()
    else:
        return None