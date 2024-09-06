import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input is empty.
    """
    if text and text.strip():
        # Remove all non-ASCII characters
        text = ''.join(char if char.isascii() else ' ' for char in text)
        # Create an MD5 hash and encode it as a hexadecimal string
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None