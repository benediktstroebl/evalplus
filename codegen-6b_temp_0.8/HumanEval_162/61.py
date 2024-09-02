
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not isinstance(text, unicode):
        return None
    if not text:
        return None
    text = to_unicode(text, encoding='utf-8')
    return hashlib.md5(text).hexdigest()


