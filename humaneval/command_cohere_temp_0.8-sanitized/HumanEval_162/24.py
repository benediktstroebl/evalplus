import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings correctly.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text and text.strip():
        # Add the hashlib library to create an MD5 hash
        md5 = hashlib.md5()
        # Encrypt the string and get the hash
        text = md5.hexdigest(text.encode()).decode()
    else:
        text = None
    return text