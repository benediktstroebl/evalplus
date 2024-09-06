import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string into MD5 and returns the result or None if the text is empty.
    """
    if text and text.strip():
        try:
            return hashlib.md5(text.encode()).hexdigest()
        except Exception as e:
            raise Exception(f"An error occurred while encrypting the string: {e}")
    else:
        return None