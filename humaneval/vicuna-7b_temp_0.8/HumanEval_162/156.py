
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Encode the string using UTF-8
    try:
        text_utf8 = text.encode('utf-8')
    except UnicodeEncodeError:
        # If the string is not encoded in UTF-8,
        # let's assume it's encoded in ASCII
        text_utf8 = text.encode('ASCII')

    # Convert the encoded string to a hash
    md5_object = hashlib.md5()
    md5_object.update(text_utf8)
    return md5_object.hexdigest()
