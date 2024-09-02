
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # BEGIN SOLUTION
    from hashlib import md5
    md5_hash = md5(text.encode())
    md5_hash = md5_hash.hexdigest()
    return md5_hash
    # END SOLUTION
