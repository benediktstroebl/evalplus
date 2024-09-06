
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    import base64

    if text == '':
        return None

    hashed = hashlib.md5(text.encode())
    b64encode = base64.b64encode(hashed.digest())
    return str(b64encode, 'utf-8')

