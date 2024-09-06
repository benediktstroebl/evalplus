import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the string text as a lowercase hexadecimal string.
    If the input is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()