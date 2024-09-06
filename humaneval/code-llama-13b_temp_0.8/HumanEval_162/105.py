
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Define md5() here.
    # import hashlib
    # md5 = hashlib.md5()

    # If the string is empty, return None.
    if not text:
        return None

    # Add 'text' to md5() hashlib.
    # md5.update(text.encode('utf-8'))
    # md5.update(text.encode())
    # md5.update(text)

    # Return the hexadecimal digest of md5().
    # return md5.hexdigest()
    return md5(text)

