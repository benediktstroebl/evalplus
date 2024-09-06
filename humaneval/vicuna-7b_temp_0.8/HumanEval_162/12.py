
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Create a new md5 hash object
    hash_object = hashlib.md5()

    # Convert the string to bytes and hash it
    hash_object.update(text.encode('utf-8'))

    # Get the hexdigest string
    return hash_object.hexdigest()
