import hashlib
def string_to_md5(text):
    """
    Compute the md5 hash of an input string and return it as a string.

    Args:
        text (str): Input string to hash.

    Returns:
        str or None: Md5 hash as a hexadecimal representation string, or None for an empty string input.
    """
    if not text:
        return None
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode())
    return md5_hash.hexdigest()