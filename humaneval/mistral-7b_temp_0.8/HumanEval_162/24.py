
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # NOTE: You may use the hashlib library for this,
    # but you should not use any other external libraries.
    # You may not use the hashlib library in any other part of the course.
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()

