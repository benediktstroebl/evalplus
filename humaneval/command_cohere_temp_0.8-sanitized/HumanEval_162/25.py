import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string, if it is not empty. None otherwise.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()