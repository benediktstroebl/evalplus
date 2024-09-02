
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text is None:
        return None
    elif text == '':
        return None
    elif isinstance(text, (str, unicode)):
        return md5(text.encode('utf-8')).hexdigest()
    else:
        raise ValueError('Expected a string, but got {0}'.format(type(text)))

