
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None

    # Make sure we are expected string
    if not isinstance(text, str):
        raise TypeError('Expect string, got %s' % type(text))

    # Make sure it is unicode
    if isinstance(text, str):
        text = text.decode('utf-8')

    # Compute string hash
    hash_ = hashlib.md5(text)
    return hash_.hexdigest()
