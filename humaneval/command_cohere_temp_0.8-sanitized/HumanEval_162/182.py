import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Args:
        text (str): The string to encrypt.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text.strip() == "":
        return None
    return hashlib.md5(text.strip().encode()).hexdigest()