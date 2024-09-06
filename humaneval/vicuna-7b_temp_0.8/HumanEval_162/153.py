
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    elif len(text) % 16 != 0:
        return None
    else:
        # Create a hash object
        hash_md5 = hashlib.md5()
        # Convert the string to bytes and hash it
        hash_md5.update(text.encode())
        return hash_md5.hexdigest()
