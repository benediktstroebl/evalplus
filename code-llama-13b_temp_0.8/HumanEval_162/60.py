
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    # A new md5 hash object
    h = hashlib.md5()

    # Some text to hash
    h.update(text.encode('utf-8'))

    # Return the encoded hex digest
    return h.hexdigest()

