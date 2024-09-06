import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None