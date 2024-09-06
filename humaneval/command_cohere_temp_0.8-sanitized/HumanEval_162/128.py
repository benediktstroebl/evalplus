import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string or None if the input is empty.
    """
    
    if text and text != "":
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()
    else:
        return None