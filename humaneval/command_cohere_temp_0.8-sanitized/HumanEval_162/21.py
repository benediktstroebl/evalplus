import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a lowercase hexadecimal string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None