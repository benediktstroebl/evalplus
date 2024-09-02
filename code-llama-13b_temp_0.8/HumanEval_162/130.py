
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    assert type(text) == str
    assert len(text) > 0

    hash_string = hashlib.md5(text.encode())
    hex_digest = hash_string.hexdigest()

    return hex_digest

