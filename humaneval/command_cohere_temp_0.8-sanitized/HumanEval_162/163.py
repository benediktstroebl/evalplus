import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.
        
    Returns:
        str or None: MD5 hash if text is not empty, otherwise None.
    """
    if text:
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None