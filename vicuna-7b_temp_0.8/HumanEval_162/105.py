
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert text to bytes
    bytes_text = bytes(text, 'utf-8')

    # Create a hash object
    hash_object = hashlib.md5()

    # Convert bytes to hash
    hash_object.update(bytes_text)

    # Get the hash in hexadecimal format
    return hash_object.hexdigest()
