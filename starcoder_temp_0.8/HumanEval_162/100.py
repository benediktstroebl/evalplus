
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # return None if text is an empty string
    if text == '':
        return None
    # convert text to md5 hash
    return hashlib.md5(text).hexdigest()

