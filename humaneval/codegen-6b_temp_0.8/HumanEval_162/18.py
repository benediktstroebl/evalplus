
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text is None or len(text) == 0:
        return None
    elif PY_M, NODE_JS, JAVASCRIPT_REMOTE:
        return text
    elif PY_PY:
        return hashlib.md5(text).hexdigest()
    else:
        return hashlib.md5(text.encode('UTF-8')).hexdigest()
