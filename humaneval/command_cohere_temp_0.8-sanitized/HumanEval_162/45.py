import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if text and text.strip():
        # Use MD5 hash function to generate the hash
        hash_value = hashlib.md5(text.encode()).hexdigest()
    else:
        hash_value = None
    
    return hash_value