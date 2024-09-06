import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts a string into MD5 and returns the result or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None