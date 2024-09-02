
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # try:
    #     import hashlib
    #     m = hashlib.md5()
    # except ImportError:
    #     import md5
    #     m = md5.new()
    #
    # try:
    #     m.update(text.encode('utf-8'))
    # except UnicodeDecodeError:
    #     m.update(text.encode('iso-8859-15'))
    #
    # return m.hexdigest()

    import hashlib
    m = hashlib.md5()

    m.update(text.encode('utf-8'))

    return m.hexdigest()

