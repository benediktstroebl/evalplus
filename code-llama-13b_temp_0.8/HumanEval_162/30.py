
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    if text == '':
        return None
    hash_object = hashlib.md5(bytes(text, 'utf-8'))
    md5_hash_str = hash_object.hexdigest()
    return md5_hash_str

