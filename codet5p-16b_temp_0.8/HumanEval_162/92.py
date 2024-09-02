
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    if len(text) == 0:
        return None

    encoded_string = text.encode()
    md5_hash = hashlib.md5(encoded_string)
    return md5_hash.hexdigest()
