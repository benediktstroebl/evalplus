
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # replace any Unicode whitespace with space
    text = text.replace(u'\u00A0', ' ')
    # strip any leading/trailing whitespace
    text = text.strip()
    # convert Unicode to ASCII
    text = text.encode('ascii', 'ignore')

    if not len(text):
        return None
    return hashlib.md5(text).hexdigest()
