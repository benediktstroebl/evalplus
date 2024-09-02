
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    try:
        # Python 3.x uses bytes, Python 2.x uses str
        return hashlib.md5(bytes(text, 'utf-8')).hexdigest()
    except UnicodeEncodeError:
        return hashlib.md5(text.encode('utf-8')).hexdigest()