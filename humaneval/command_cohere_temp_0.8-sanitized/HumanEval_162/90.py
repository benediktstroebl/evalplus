import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a lowercase hexadecimal string.
    Empty text returns None.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()