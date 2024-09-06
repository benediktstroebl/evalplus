import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Compute the MD5 hash of the given string or return None for an empty input.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a lowercase hexadecimal string, or None for empty input.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest().lower()