
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # This algorithm is not required to return an md5 hash,
    # but it is required to be an md5 hash.
    if text == '':
        return None
    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()

