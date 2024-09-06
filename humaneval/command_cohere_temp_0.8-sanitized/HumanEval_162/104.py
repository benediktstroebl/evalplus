import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a string, or None if the input is empty.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()