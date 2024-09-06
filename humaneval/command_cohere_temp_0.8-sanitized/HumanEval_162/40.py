import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    For an empty string, returns None.

    :param text: String to encrypt
    :return: MD5 encrypted string or None
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()