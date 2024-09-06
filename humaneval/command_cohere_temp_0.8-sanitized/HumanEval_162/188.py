import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string into MD5 and returns the result.
    For an empty string, returns None.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()