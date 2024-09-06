import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts a string into MD5 and returns the result or None if the input is empty.

    Args:
        text (str): The string to be encrypted.

    Returns:
        str or None: The MD5 hash of the input string or None if the input is empty.
    """
    if text and text.strip():
        try:
            return hashlib.md5(text.encode()).hexdigest()
        except Exception as e:
            raise ValueError(f"An error occurred while encrypting the string: {e}")
    else:
        return None