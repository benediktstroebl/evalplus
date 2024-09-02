
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Hint: Look up the md5 hash function from the python standard library.
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()

