
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    from hashlib import md5
    md5_instance = md5()
    md5_instance.update(text.encode('utf-8'))
    return md5_instance.hexdigest()
