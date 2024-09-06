
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text is None: return None
    if not (type(text) is str or type(text) is unicode):
        text = str(text)
    if text and not text.isspace():
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    else:
        return None

