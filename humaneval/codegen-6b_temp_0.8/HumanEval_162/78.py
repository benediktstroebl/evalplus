
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Check for unicode.
    if isinstance(text, six.text_type):
        text = text.encode('utf-8')

    return hashlib.md5(text).hexdigest()
