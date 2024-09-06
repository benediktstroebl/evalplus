
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # http://stackoverflow.com/a/2257449/33338
    if not text:
        return None
    return hashlib.md5(text.encode("utf-8")).hexdigest()
