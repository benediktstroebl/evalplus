
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert the string to bytes and then to hex
    hash_val = hashlib.md5(bytes(text, 'utf-8')).hexdigest()

    return hash_val
